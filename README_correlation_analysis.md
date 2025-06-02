# News-Stock Correlation Analysis Script

## Overview

This Python script performs comprehensive analysis of the correlation between news sentiment and stock price movements. It's designed to handle the complete pipeline from data loading to generating detailed reports and visualizations.

## Features

### 1. Date Alignment

- Automatically aligns news and stock price datasets by dates
- Handles different date formats and timestamp normalization
- Aggregates multiple news articles per day into daily sentiment scores

### 2. Sentiment Analysis

- **NLTK VADER**: Advanced sentiment analysis specifically tuned for social media text
- **TextBlob**: Provides polarity and subjectivity scores
- **Multi-method approach**: Combines multiple sentiment analysis techniques for robustness
- **Sentiment categorization**: Classifies sentiment as positive, negative, or neutral

### 3. Stock Returns Calculation

- Computes daily percentage changes in closing prices
- Calculates technical indicators (moving averages, volatility)
- Handles volume and price change metrics

### 4. Correlation Analysis

- **Pearson correlation**: Measures linear relationships
- **Spearman correlation**: Captures monotonic relationships
- **Lag analysis**: Tests predictive power of previous days' sentiment (1-5 day lags)
- **Category analysis**: Compares returns across sentiment categories
- **Volume correlation**: Analyzes relationship between sentiment and trading volume

### 5. Comprehensive Reporting

- Statistical significance testing
- Detailed correlation matrices
- Visual analytics with 6 different chart types
- Exportable reports in text format

## Installation

1. Install required dependencies:

```bash
pip install -r requirements_correlation_analysis.txt
```

2. Download NLTK data (automatically handled by the script):

```python
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
```

## Usage

### Basic Usage

```python
from scripts.news_stock_correlation_analysis import NewsStockCorrelationAnalyzer

# Initialize analyzer
analyzer = NewsStockCorrelationAnalyzer(data_dir='data')

# Run complete analysis for specific symbols
analyzer.run_complete_analysis(
    symbols=['AAPL', 'TSLA', 'NVDA'],
    save_results=True,
    output_dir='correlation_results'
)
```

### Advanced Usage

```python
# Step-by-step analysis for more control
analyzer = NewsStockCorrelationAnalyzer()

# 1. Load data
analyzer.load_stock_data(['AAPL', 'TSLA'])
analyzer.load_news_data()

# 2. Process sentiment
analyzer.process_news_sentiment()

# 3. Analyze specific symbol
analyzer.align_data_by_date('AAPL')
correlations = analyzer.calculate_correlations('AAPL', lag_days=7)

# 4. Generate visualizations
analyzer.generate_visualizations('AAPL', save_path='results')

# 5. Generate report
report = analyzer.generate_report('AAPL')
print(report)
```

### Customizing Analysis

```python
# Custom news data file
analyzer.load_news_data('path/to/custom_news.csv')

# Custom correlation analysis
correlations = analyzer.calculate_correlations('AAPL', lag_days=10)

# Generate only specific visualizations
analyzer.generate_visualizations('AAPL')  # Display only
```

## Input Data Requirements

### Stock Data

- **Format**: CSV files with columns: Date, Open, High, Low, Close, Volume
- **Location**: `data/yfinance_data/{SYMBOL}_historical_data.csv`
- **Date format**: Any pandas-parseable format

### News Data

- **Format**: CSV file with news articles/analyst ratings
- **Required columns**:
  - Date column (various names supported: 'date', 'Date', 'publish_date', 'timestamp')
  - Text column (various names supported: 'headline', 'title', 'text', 'summary', 'content')
  - Optional symbol column for symbol-specific filtering
- **Location**: `data/raw_analyst_ratings.csv` (default)

## Output

### 1. Correlation Reports

- Statistical correlation coefficients
- P-values for significance testing
- Lag analysis results
- Sentiment category breakdowns
- Key insights and interpretations

### 2. Visualizations

- Time series plots of sentiment vs returns
- Scatter plots with trend lines
- Box plots by sentiment category
- Lag correlation bar charts
- Return distribution comparisons
- Sentiment distribution pie charts

### 3. Data Files

- Aligned datasets with sentiment scores
- Processed correlation matrices
- Summary statistics

## Methodology

### Sentiment Analysis

- **VADER (Valence Aware Dictionary and sEntiment Reasoner)**: Specifically designed for social media text, provides compound scores from -1 (negative) to +1 (positive)
- **TextBlob**: Provides polarity (-1 to +1) and subjectivity (0 to 1) scores
- **Aggregation**: Daily sentiment scores are averaged across all news articles for each day

### Statistical Analysis

- **Pearson Correlation**: Measures linear relationships between sentiment and returns
- **Spearman Correlation**: Captures monotonic (non-linear) relationships
- **Significance Testing**: Uses α=0.05 threshold for statistical significance
- **Lag Analysis**: Tests whether previous days' sentiment predicts current returns

### Correlation Interpretation

- **|r| < 0.1**: Negligible correlation
- **0.1 ≤ |r| < 0.3**: Weak correlation
- **0.3 ≤ |r| < 0.5**: Moderate correlation
- **0.5 ≤ |r| < 0.7**: Strong correlation
- **|r| ≥ 0.7**: Very strong correlation

## Example Output

```
========================================
NEWS SENTIMENT - STOCK CORRELATION REPORT
========================================
Symbol: AAPL
Analysis Date: 2024-01-15 14:30:25
========================================

DATA SUMMARY:
- Total trading days analyzed: 1,250
- Days with news coverage: 890 (71.2%)
- Average daily return: 0.0012 (0.12%)
- Return volatility (std): 0.0234
- Average sentiment score: 0.0456
- Sentiment volatility (std): 0.1234

CORRELATION ANALYSIS:

Primary Correlations (Same-day):
- Pearson correlation: 0.0234 (p-value: 0.4321)
- Spearman correlation: 0.0187 (p-value: 0.5432)
→ The negligible positive correlation is not statistically significant at α=0.05 level.

Lag Analysis (Previous days' sentiment vs current returns):
- Lag 1 day: -0.0123 (p=0.6789, not significant)
- Lag 2 day: 0.0456 (p=0.1234, not significant)
- Lag 3 day: 0.0789 (p=0.0234, significant)

KEY INSIGHTS:
• No significant relationship found between same-day news sentiment and stock returns
• Strongest predictive sentiment effect found at 3-day lag (r=0.079)
• Positive sentiment days show higher average returns (0.0015 vs -0.0008)
```

## Error Handling

The script includes robust error handling for:

- Missing data files
- Malformed CSV data
- Date parsing issues
- Memory management for large datasets
- Network timeout for NLTK downloads

## Performance Considerations

- **Memory Usage**: Processes large news datasets in chunks
- **Processing Time**: Sentiment analysis is performed in batches with progress indicators
- **Scalability**: Designed to handle datasets with millions of news articles
- **Caching**: Results are cached to avoid recomputation

## Troubleshooting

### Common Issues

1. **NLTK Download Errors**:

   ```bash
   python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('punkt')"
   ```

2. **Memory Issues with Large Datasets**:

   - Reduce chunk size in `load_news_data()`
   - Process fewer symbols at once

3. **Date Alignment Problems**:

   - Check date column formats in both datasets
   - Ensure timezone consistency

4. **No Correlation Found**:
   - Verify data quality and date ranges
   - Check if news data is relevant to stock symbols
   - Consider different lag periods

## Contributing

When extending this script:

1. Maintain the modular class structure
2. Add comprehensive error handling
3. Include progress indicators for long-running operations
4. Update documentation for new features
5. Test with different data formats and sizes

## License

This script is part of the "Predicting Price Moves with News Sentiment" project and follows the same licensing terms.
