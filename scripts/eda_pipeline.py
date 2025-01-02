import pandas as pd
from logger import setup_logger

logger = setup_logger("EDA")

def load_data(file_path):
    """Load dataset"""
    try:
        logger.info(f"Loading data from {file_path}")
        return pd.read_csv(file_path)
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise

def clean_data(df):
    """Handle missing values and outliers"""
    logger.info("Cleaning data: handling missing values and outliers.")
    # Fill missing values in CompetitionDistance with median
    df['CompetitionDistance'].fillna(df['CompetitionDistance'].median(), inplace=True)
    # Fill missing PromoInterval with 'None'
    df['PromoInterval'].fillna('None', inplace=True)
    # Drop rows where stores are closed (Open = 0)
    df = df[df['Open'] == 1]
    return df
