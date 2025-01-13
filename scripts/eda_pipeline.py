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

class CleanedData:
    """Class to handle data cleaning tasks including missing values and outliers."""

   
    def check_missing_data(df: pd.DataFrame) -> pd.Series:
        """Check for missing values in the dataset."""
        missing_data = df.isnull().sum()
        missing_data = missing_data[missing_data > 0]
        logger.info(f"Missing data: {missing_data}")
        return missing_data
    
    def handle_missing_values_for_store(df: pd.DataFrame) -> pd.DataFrame:
        """Handle missing values and prepare the store dataset."""
        logger.info("Handling missing values for store data.")
        df['CompetitionDistance'] = df['CompetitionDistance'].fillna(df['CompetitionDistance'].median())
        df['CompetitionOpenSinceMonth'] = df['CompetitionOpenSinceMonth'].fillna(0)
        df['CompetitionOpenSinceYear'] = df['CompetitionOpenSinceYear'].fillna(0)
        df['Promo2SinceYear'] = df['Promo2SinceYear'].fillna(0)
        df['Promo2SinceWeek'] = df['Promo2SinceWeek'].fillna(0)
        df['PromoInterval'] = df['PromoInterval'].fillna('None')
        return df

    
    def handle_missing_values_for_train(df: pd.DataFrame) -> pd.DataFrame:
        """Handle missing values in the train dataset."""
        logger.info("Handling missing values for train data.")
        df.dropna(subset=['Open'], inplace=True)
        return df

    
    def clean_data(df: pd.DataFrame) -> pd.DataFrame:
        """Handle missing values and prepare data by removing outliers."""
        logger.info("Cleaning data: handling missing values and outliers.")
        df['CompetitionDistance'] = df['CompetitionDistance'].fillna(df['CompetitionDistance'].median())
        df['PromoInterval'] = df['PromoInterval'].fillna('None')
        df = df[df['Open'] == 1]
        return df

