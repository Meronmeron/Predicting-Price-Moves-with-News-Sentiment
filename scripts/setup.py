#!/usr/bin/env python3
"""
Environment Setup Script

This script sets up the complete development environment including:
- Virtual environment creation
- Dependencies installation
- Pre-commit hooks setup
- Directory structure validation
"""

import os
import sys
import subprocess
import argparse
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def run_command(command, check=True, shell=True):
    """Run a shell command and return the result."""
    logger.info(f"Running: {command}")
    try:
        result = subprocess.run(
            command, 
            shell=shell, 
            check=check, 
            capture_output=True, 
            text=True
        )
        if result.stdout:
            logger.info(result.stdout.strip())
        return result
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {e}")
        if e.stderr:
            logger.error(e.stderr)
        if check:
            sys.exit(1)
        return e


def check_python_version():
    """Check if Python version is 3.8 or higher."""
    logger.info("Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        logger.error("Python 3.8 or higher is required!")
        sys.exit(1)
    logger.info(f"Python {version.major}.{version.minor}.{version.micro} - OK")


def create_venv(venv_path="venv", dry_run=False):
    """Create virtual environment."""
    logger.info(f"Creating virtual environment at {venv_path}...")
    
    if Path(venv_path).exists():
        logger.warning(f"Virtual environment {venv_path} already exists!")
        return
    
    if dry_run:
        logger.info(f"[DRY RUN] Would create virtual environment: python -m venv {venv_path}")
        return
    
    run_command(f"python -m venv {venv_path}")
    logger.info("Virtual environment created successfully!")


def get_activation_command():
    """Get the activation command based on OS."""
    if os.name == 'nt':  # Windows
        return "venv\\Scripts\\activate"
    else:  # Unix/Linux/MacOS
        return "source venv/bin/activate"


def install_dependencies(venv_path="venv", dry_run=False):
    """Install project dependencies."""
    logger.info("Installing dependencies...")
    
    # Determine pip path based on OS
    if os.name == 'nt':  # Windows
        pip_path = Path(venv_path) / "Scripts" / "pip"
    else:  # Unix/Linux/MacOS
        pip_path = Path(venv_path) / "bin" / "pip"
    
    if dry_run:
        logger.info(f"[DRY RUN] Would upgrade pip: {pip_path} install --upgrade pip")
        if Path("requirements.txt").exists():
            logger.info(f"[DRY RUN] Would install requirements: {pip_path} install -r requirements.txt")
        else:
            logger.warning("[DRY RUN] requirements.txt not found!")
        return
    
    # Upgrade pip first
    run_command(f'"{pip_path}" install --upgrade pip')
    
    # Install requirements
    if Path("requirements.txt").exists():
        run_command(f'"{pip_path}" install -r requirements.txt')
    else:
        logger.warning("requirements.txt not found!")
    
    logger.info("Dependencies installed successfully!")


def setup_pre_commit(venv_path="venv", dry_run=False):
    """Setup pre-commit hooks."""
    logger.info("Setting up pre-commit hooks...")
    
    # Determine python path
    if os.name == 'nt':  # Windows
        python_path = Path(venv_path) / "Scripts" / "python"
    else:  # Unix/Linux/MacOS
        python_path = Path(venv_path) / "bin" / "python"
    
    # Create .pre-commit-config.yaml if it doesn't exist
    pre_commit_config = """repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
    -   id: check-merge-conflict
-   repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
    -   id: black
        language_version: python3
-   repo: https://github.com/pycqa/flake8
    rev: 5.0.4
    hooks:
    -   id: flake8
        args: [--max-line-length=88, --extend-ignore=E203,W503]
"""
    
    if not Path(".pre-commit-config.yaml").exists():
        if dry_run:
            logger.info("[DRY RUN] Would create .pre-commit-config.yaml")
        else:
            with open(".pre-commit-config.yaml", "w") as f:
                f.write(pre_commit_config)
            logger.info("Created .pre-commit-config.yaml")
    
    # Install pre-commit hooks
    if dry_run:
        logger.info(f"[DRY RUN] Would install pre-commit hooks: {python_path} -m pre_commit install")
    else:
        run_command(f'"{python_path}" -m pre_commit install')
        logger.info("Pre-commit hooks installed successfully!")


def validate_structure():
    """Validate project directory structure."""
    logger.info("Validating project structure...")
    
    required_dirs = [
        "src",
        "tests", 
        "notebooks",
        "scripts",
        ".github/workflows",
        ".vscode"
    ]
    
    required_files = [
        "requirements.txt",
        "README.md",
        ".gitignore",
        "src/__init__.py",
        "tests/__init__.py",
        "notebooks/__init__.py",
        "scripts/__init__.py"
    ]
    
    for directory in required_dirs:
        if not Path(directory).exists():
            logger.warning(f"Directory missing: {directory}")
        else:
            logger.info(f"✓ {directory}")
    
    for file in required_files:
        if not Path(file).exists():
            logger.warning(f"File missing: {file}")
        else:
            logger.info(f"✓ {file}")


def create_sample_config(dry_run=False):
    """Create sample configuration files."""
    logger.info("Creating sample configuration files...")
    
    # Create config directory
    config_dir = Path("config")
    
    if dry_run:
        logger.info(f"[DRY RUN] Would create config directory: {config_dir}")
    else:
        config_dir.mkdir(exist_ok=True)
    
    # Create sample config
    sample_config = """# Sample Configuration File
project:
  name: "Predicting Price Moves"
  version: "0.1.0"

data:
  symbols: ["AAPL", "GOOGL", "MSFT", "AMZN"]
  start_date: "2020-01-01"
  news_sources: ["reuters", "bloomberg"]

models:
  random_forest:
    n_estimators: 100
    max_depth: 10
  xgboost:
    learning_rate: 0.1
    n_estimators: 100

training:
  test_size: 0.2
  validation_size: 0.1
  random_state: 42
"""
    
    config_file = config_dir / "default.yaml"
    if not config_file.exists():
        if dry_run:
            logger.info("[DRY RUN] Would create config/default.yaml")
        else:
            with open(config_file, "w") as f:
                f.write(sample_config)
            logger.info("Created config/default.yaml")


def main():
    """Main setup function."""
    parser = argparse.ArgumentParser(description="Setup development environment")
    parser.add_argument(
        "--venv-path", 
        default="venv", 
        help="Virtual environment path (default: venv)"
    )
    parser.add_argument(
        "--skip-venv", 
        action="store_true", 
        help="Skip virtual environment creation"
    )
    parser.add_argument(
        "--skip-deps", 
        action="store_true", 
        help="Skip dependency installation"
    )
    parser.add_argument(
        "--skip-hooks", 
        action="store_true", 
        help="Skip pre-commit hooks setup"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without executing"
    )
    
    args = parser.parse_args()
    
    if args.dry_run:
        logger.info("🔍 DRY RUN MODE - No actual operations will be performed")
    
    logger.info("Starting environment setup...")
    
    # Check Python version
    check_python_version()
    
    # Validate project structure
    validate_structure()
    
    # Create virtual environment
    if not args.skip_venv:
        create_venv(args.venv_path, args.dry_run)
    
    # Install dependencies
    if not args.skip_deps:
        install_dependencies(args.venv_path, args.dry_run)
    
    # Setup pre-commit hooks
    if not args.skip_hooks:
        setup_pre_commit(args.venv_path, args.dry_run)
    
    # Create sample configuration
    create_sample_config(args.dry_run)
    
    logger.info("🎉 Setup completed successfully!")
    logger.info(f"To activate the virtual environment, run:")
    logger.info(f"  {get_activation_command()}")
    logger.info("Then you can start working on the project!")


if __name__ == "__main__":
    main() 