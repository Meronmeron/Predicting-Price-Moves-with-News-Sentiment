# Exploratory Data Analysis (EDA) Notebook

## Overview

This notebook provides a comprehensive exploratory data analysis of the news sentiment dataset for predicting price movements. The analysis covers all the requested aspects:

- **Descriptive Statistics**: Basic statistics for textual lengths and article counts
- **Text Analysis and Topic Modeling**: NLP techniques to identify keywords and topics
- **Time Series Analysis**: Publication patterns and frequency analysis
- **Publisher Analysis**: Analysis of publisher activity and specialization

## Files in this directory

- `eda_news_sentiment_analysis.ipynb` - Main EDA notebook
- `create_eda_notebook.py` - Script used to generate the notebook
- `test_notebook.py` - Test script to verify functionality
- `setup_dependencies.py` - Automated dependency installer
- `EDA_README.md` - This documentation file

## Quick Setup

### Option 1: Automated Setup (Recommended)

Run the automated setup script:

```bash
python setup_dependencies.py
```

This will automatically check and install all required packages.

### Option 2: Manual Setup

1. Make sure you have activated your virtual environment:

   ```bash
   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

2. Install required packages:

   ```bash
   pip install -r ../requirements.txt
   pip install wordcloud scikit-learn nltk textblob plotly seaborn
   ```

   **Note**: Use `nltk` (not `ntlk`) and `scikit-learn` (not `sklearn`)

### Running the Analysis

1. Start Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

2. Open `eda_news_sentiment_analysis.ipynb`

3. Run all cells or execute cell by cell

## Common Installation Issues & Fixes

### ❌ Error: `ntlk` not found

**Fix**: Use the correct spelling: `pip install nltk`

### ❌ Error: `sklearn` deprecated

**Fix**: Use `pip install scikit-learn` instead of `sklearn`

### ❌ Error: Missing NLTK data

**Fix**: The notebook automatically downloads required NLTK data, or run:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

### ❌ Memory issues with large dataset

**Fix**: The notebook includes sampling options for memory efficiency

## Analysis Sections

### 1. Data Loading and Initial Exploration

- Loads the `raw_analyst_ratings.csv` dataset
- Displays basic information about the dataset structure
- Creates time-based features and text metrics

### 2. Descriptive Statistics

- **Headline Length Analysis**: Distribution of character and word counts
- **Publisher Activity**: Most active publishers and article counts
- **Publication Trends**: Daily publication frequency over time

### 3. Text Analysis and Topic Modeling

- **Text Preprocessing**: Cleaning and normalizing headlines
- **Word Frequency Analysis**: Most common words and phrases
- **Financial Keywords**: Detection of financial terms like "FDA approval", "price target"
- **Topic Modeling**: LDA topic discovery to identify themes
- **Word Cloud**: Visual representation of common terms

### 4. Time Series Analysis

- **Daily Patterns**: Publication frequency by day of week
- **Hourly Patterns**: When news is published throughout the day
- **Monthly Trends**: Long-term publication trends
- **Publication Spikes**: Detection of unusual news activity days
- **Market Hours vs After Hours**: Analysis of publication timing

### 5. Publisher Analysis

- **Domain Extraction**: Identifying unique organizations from email addresses
- **Publisher Specialization**: Which publishers focus on specific stocks
- **Activity Patterns**: Publisher activity spans and consistency
- **Market Concentration**: How concentrated the news sources are

### 6. Key Insights and Conclusions

- Comprehensive summary of findings
- Data quality assessment
- Recommendations for further analysis

## Expected Outputs

The notebook will generate:

1. **Visualizations**:

   - Histograms and box plots of headline lengths
   - Bar charts of publisher activity
   - Time series plots of publication trends
   - Word clouds and frequency charts
   - Publication pattern analysis

2. **Statistical Summaries**:

   - Descriptive statistics for all numerical variables
   - Publisher concentration metrics
   - Time-based publication patterns
   - Text analysis results

3. **Data Files**:
   - `../data/processed_news_sample.csv` - Sample of processed data
   - `../data/eda_summary.json` - Key statistics summary

## Technical Details

### Libraries Used

- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn, plotly
- **Text Analysis**: nltk, scikit-learn, wordcloud, textblob
- **Topic Modeling**: Latent Dirichlet Allocation (LDA)

### Performance Considerations

- The notebook includes error handling for missing dependencies
- Large datasets are sampled for memory efficiency
- Processing time varies based on dataset size (313MB original file)

## Verification

To verify everything is working, run:

```bash
python -c "import pandas, numpy, matplotlib, seaborn, plotly, nltk, sklearn, wordcloud, textblob; print('✅ All packages ready!')"
```

## Next Steps

After running this EDA, consider:

1. **Sentiment Analysis**: Add sentiment scoring to headlines
2. **Stock Price Correlation**: Correlate news volume with price movements
3. **Predictive Modeling**: Use insights to build prediction models
4. **Real-time Analysis**: Adapt for live news feeds
5. **Publisher Bias Analysis**: Study publisher-specific patterns

## Data Understanding

The dataset contains:

- **headline**: News headline text
- **url**: Article URL
- **publisher**: News source (often email format)
- **date**: Publication timestamp
- **stock**: Stock ticker symbol

This EDA provides the foundation for understanding patterns in financial news that could be predictive of stock price movements.
