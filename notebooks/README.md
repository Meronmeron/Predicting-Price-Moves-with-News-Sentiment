# Notebooks Directory

This directory contains Jupyter notebooks for various aspects of the project:

## 📁 Structure

```
notebooks/
├── __init__.py
├── README.md
├── 01_data_exploration/
│   ├── data_overview.ipynb
│   ├── market_analysis.ipynb
│   └── news_sentiment_eda.ipynb
├── 02_feature_engineering/
│   ├── technical_indicators.ipynb
│   ├── sentiment_features.ipynb
│   └── feature_selection.ipynb
├── 03_model_development/
│   ├── baseline_models.ipynb
│   ├── advanced_models.ipynb
│   └── model_comparison.ipynb
├── 04_model_evaluation/
│   ├── performance_metrics.ipynb
│   ├── backtesting.ipynb
│   └── risk_analysis.ipynb
└── 05_experiments/
    ├── hyperparameter_tuning.ipynb
    └── feature_importance.ipynb
```

## 🚀 Getting Started

### 1. Start Jupyter

```bash
# From project root
jupyter notebook notebooks/
```

### 2. Notebook Categories

#### 📊 Data Exploration (01_data_exploration/)

- **data_overview.ipynb**: Initial data exploration and statistics
- **market_analysis.ipynb**: Market trend analysis and visualization
- **news_sentiment_eda.ipynb**: News data and sentiment analysis exploration

#### 🔧 Feature Engineering (02_feature_engineering/)

- **technical_indicators.ipynb**: Creating technical analysis indicators
- **sentiment_features.ipynb**: Building sentiment-based features
- **feature_selection.ipynb**: Feature selection and dimensionality reduction

#### 🤖 Model Development (03_model_development/)

- **baseline_models.ipynb**: Simple baseline models
- **advanced_models.ipynb**: Complex ML models (ensemble, neural networks)
- **model_comparison.ipynb**: Comparing different model architectures

#### 📈 Model Evaluation (04_model_evaluation/)

- **performance_metrics.ipynb**: Detailed performance analysis
- **backtesting.ipynb**: Historical backtesting strategies
- **risk_analysis.ipynb**: Risk metrics and analysis

#### 🧪 Experiments (05_experiments/)

- **hyperparameter_tuning.ipynb**: Optimizing model parameters
- **feature_importance.ipynb**: Understanding feature contributions

## 📝 Best Practices

### Notebook Structure

1. **Clear Title and Description**
2. **Import Section**: All imports at the top
3. **Configuration**: Set random seeds, plotting style
4. **Data Loading**: Load and validate data
5. **Analysis/Development**: Main content
6. **Conclusions**: Summary of findings
7. **Next Steps**: What to do next

### Code Quality

- Keep cells focused and concise
- Add markdown explanations between code sections
- Use descriptive variable names
- Include data validation checks
- Save important results/plots

### Version Control

- Clear notebooks before committing (`jupyter nbconvert --clear-output`)
- Use meaningful commit messages
- Consider using `nbstripout` for automatic output removal

## 📊 Visualization Guidelines

- Use consistent color schemes
- Add proper titles and axis labels
- Include data source information
- Make plots publication-ready
- Save important plots to `results/figures/`

## 🔗 Integration with Source Code

Notebooks should primarily be used for:

- Exploration and experimentation
- Visualization and reporting
- Prototyping new features

Production code should be moved to the `src/` directory as Python modules.

## 💡 Tips

1. **Start each notebook with environment setup**:

   ```python
   import sys
   sys.path.append('../')

   import warnings
   warnings.filterwarnings('ignore')

   %matplotlib inline
   %load_ext autoreload
   %autoreload 2
   ```

2. **Use relative imports from src**:

   ```python
   from src.data import DataCollector
   from src.models import PricePredictionModel
   ```

3. **Set random seeds for reproducibility**:

   ```python
   import numpy as np
   import random

   SEED = 42
   np.random.seed(SEED)
   random.seed(SEED)
   ```
