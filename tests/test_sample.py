"""
Sample Test Module

This module contains sample tests to demonstrate the testing structure
and ensure the CI/CD pipeline works correctly.
"""

import unittest
import sys
from pathlib import Path

# Add src to path for imports
sys.path.append(str(Path(__file__).parent.parent))


class TestSampleFunctionality(unittest.TestCase):
    """Test class for sample functionality."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_data = [1, 2, 3, 4, 5]
        self.expected_sum = 15

    def test_basic_math(self):
        """Test basic mathematical operations."""
        result = sum(self.test_data)
        self.assertEqual(result, self.expected_sum)

    def test_list_operations(self):
        """Test list operations."""
        test_list = [1, 2, 3]
        test_list.append(4)
        self.assertEqual(len(test_list), 4)
        self.assertIn(4, test_list)

    def test_string_operations(self):
        """Test string operations."""
        test_string = "Hello World"
        self.assertTrue(test_string.startswith("Hello"))
        self.assertTrue(test_string.endswith("World"))
        self.assertEqual(len(test_string), 11)

    def test_dictionary_operations(self):
        """Test dictionary operations."""
        test_dict = {"key1": "value1", "key2": "value2"}
        self.assertIn("key1", test_dict)
        self.assertEqual(test_dict["key1"], "value1")
        self.assertEqual(len(test_dict), 2)

    def tearDown(self):
        """Clean up after each test method."""
        # Cleanup code would go here
        pass


class TestEnvironmentSetup(unittest.TestCase):
    """Test environment setup and configuration."""

    def test_python_version(self):
        """Test that Python version is appropriate."""
        version = sys.version_info
        self.assertGreaterEqual(version.major, 3)
        self.assertGreaterEqual(version.minor, 8)

    def test_import_availability(self):
        """Test that required imports are available."""
        try:
            import numpy
            import pandas
            import sklearn
            # If we get here, imports are successful
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Required package not available: {e}")

    def test_file_structure(self):
        """Test that project structure exists."""
        project_root = Path(__file__).parent.parent
        
        required_dirs = [
            "src",
            "tests",
            "notebooks",
            "scripts"
        ]
        
        for directory in required_dirs:
            dir_path = project_root / directory
            self.assertTrue(
                dir_path.exists(), 
                f"Required directory {directory} does not exist"
            )


if __name__ == "__main__":
    unittest.main() 