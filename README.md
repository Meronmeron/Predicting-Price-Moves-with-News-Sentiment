# Predicting Price Moves with News Sentiment

A machine learning project that predicts stock price movements using news sentiment analysis and technical indicators.

## 🚀 Features

- **News Sentiment Analysis**: Extract and analyze sentiment from financial news
- **Technical Indicators**: Implement various technical analysis indicators
- **Machine Learning Models**: Multiple ML models for price prediction
- **Real-time Data**: Integration with financial data APIs
- **Comprehensive Testing**: Full test suite with CI/CD pipeline

## 📋 Requirements

- Python 3.8+
- Virtual environment (recommended)
- Git

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Predicting_Price_moves
```

### 2. Set up virtual environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set up pre-commit hooks (optional but recommended)

```bash
pre-commit install
```

## 📁 Project Structure

```
├── .vscode/                 # VS Code settings
│   └── settings.json
├── .github/                 # GitHub workflows
│   └── workflows/
│       └── unittests.yml
├── .gitignore              # Git ignore rules
├── requirements.txt        # Project dependencies
├── README.md              # Project documentation
├── src/                   # Source code
│   ├── __init__.py
│   ├── data/              # Data processing modules
│   ├── models/            # ML models
│   ├── features/          # Feature engineering
│   └── utils/             # Utility functions
├── notebooks/             # Jupyter notebooks
│   ├── __init__.py
│   ├── README.md
│   └── exploratory/       # EDA notebooks
├── tests/                 # Test files
│   ├── __init__.py
│   ├── test_data/
│   ├── test_models/
│   └── test_utils/
└── scripts/               # Utility scripts
    ├── __init__.py
    ├── README.md
    ├── setup.py          # Environment setup
    └── run_pipeline.py   # Main pipeline script
```

## 🚀 Quick Start

### 1. Data Collection

```python
from src.data import DataCollector

collector = DataCollector()
stock_data = collector.get_stock_data('AAPL', start='2020-01-01')
news_data = collector.get_news_data('AAPL')
```

### 2. Feature Engineering

```python
from src.features import FeatureEngineer

engineer = FeatureEngineer()
features = engineer.create_technical_indicators(stock_data)
sentiment_features = engineer.analyze_sentiment(news_data)
```

### 3. Model Training

```python
from src.models import PricePredictionModel

model = PricePredictionModel()
model.train(features, target)
predictions = model.predict(test_features)
```

## 📊 Usage Examples

### Running Jupyter Notebooks

```bash
jupyter notebook notebooks/
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_models/test_prediction_model.py
```

### Code Formatting

```bash
# Format code
black src/ tests/ scripts/

# Check code style
flake8 src/ tests/ scripts/

# Lint code
pylint src/
```

## 🧪 Testing

The project includes comprehensive testing:

- **Unit Tests**: Test individual components
- **Integration Tests**: Test component interactions
- **End-to-End Tests**: Test complete workflows
- **Performance Tests**: Test model performance metrics

Run tests with:

```bash
pytest tests/ -v
```

## 🔄 CI/CD Pipeline

The project uses GitHub Actions for continuous integration:

- **Code Quality**: Linting with flake8 and pylint
- **Testing**: Automated testing across Python 3.8-3.11
- **Coverage**: Code coverage reporting
- **Formatting**: Code formatting checks with black

## 📈 Performance Metrics

- **Accuracy**: Model prediction accuracy
- **Precision/Recall**: Classification metrics
- **Sharpe Ratio**: Risk-adjusted returns
- **Maximum Drawdown**: Risk metrics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Code Style

This project follows:

- **PEP 8**: Python style guide
- **Black**: Code formatting
- **Type Hints**: For better code documentation
- **Docstrings**: Google-style docstrings

## 🔗 APIs and Data Sources

- **Yahoo Finance**: Historical stock data
- **Alpha Vantage**: Real-time financial data
- **News APIs**: Financial news and sentiment data

## ⚠️ Disclaimer

This project is for educational and research purposes only. It should not be used as the sole basis for investment decisions. Always consult with a qualified financial advisor before making investment decisions.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Financial data providers
- Open source ML libraries
- Python community contributions
