import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, filename='eda.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class SalesAnalysis:
    """Class for performing various sales analyses."""

    def __init__(self, df):
        self.df = df
        self.df['Date'] = pd.to_datetime(self.df['Date'])

    def analyze_holiday_sales(self):
        """Analyze sales behavior before, during, and after holidays."""
        logging.info("Analyzing sales behavior before, during, and after holidays.")
        self.df['StateHoliday'] = self.df['StateHoliday'].astype(str)
        self.df = self.df.sort_values(by='Date')
        self.df['IsHoliday'] = self.df['StateHoliday'].isin(['a', 'b', 'c'])

        for holiday in ['a', 'b', 'c']:
            self.df[f'Before_{holiday}'] = self.df['StateHoliday'].shift(-1, fill_value='0') == holiday
            self.df[f'After_{holiday}'] = self.df['StateHoliday'].shift(1, fill_value='0') == holiday

        self.df['HolidayCategory'] = 'Normal'
        for holiday in ['a', 'b', 'c']:
            self.df.loc[self.df['StateHoliday'] == holiday, 'HolidayCategory'] = f'During {holiday.upper()}'
            self.df.loc[self.df[f'Before_{holiday}'], 'HolidayCategory'] = f'Before {holiday.upper()}'
            self.df.loc[self.df[f'After_{holiday}'], 'HolidayCategory'] = f'After {holiday.upper()}'

        plt.figure(figsize=(12, 6))
        sns.barplot(x='HolidayCategory', y='Sales', data=self.df, hue='HolidayCategory', palette='viridis')
        plt.title("Average Sales Before, During, and After Holidays")
        plt.xticks(rotation=45)
        plt.show()

    def analyze_seasonality(self):
        """Analyze seasonal purchasing behaviors."""
        logging.info("Analyzing seasonal purchasing behaviors.")
        self.df['Month'] = self.df['Date'].dt.month
        seasonal_sales = self.df.groupby('Month')['Sales'].mean().reset_index()

        plt.figure(figsize=(12, 6))
        sns.barplot(x='Month', y='Sales', data=seasonal_sales, hue='Month', palette='coolwarm')
        plt.title("Average Sales Per Month")
        plt.show()

    def analyze_store_open_close(self):
        """Analyze customer behavior during store opening and closing times."""
        logging.info("Analyzing trends during store open/close.")
        open_sales = self.df.groupby('Open')['Sales'].mean().reset_index()

        plt.figure(figsize=(8, 5))
        sns.barplot(x='Open', y='Sales', data=open_sales, hue='Open', palette='coolwarm')
        plt.title("Average Sales When Store Is Open vs Closed")
        plt.show()

    def analyze_weekday_weekend_sales(self):
        """Analyze sales trends for stores open all weekdays and their weekend performance."""
        logging.info("Analyzing sales trends for weekday-open stores during weekends.")
        weekday_open_stores = self.df[self.df['DayOfWeek'].isin([1, 2, 3, 4, 5]) & (self.df['Open'] == 1)]['Store'].unique()
        weekend_sales = self.df[(self.df['Store'].isin(weekday_open_stores)) & (self.df['DayOfWeek'].isin([6, 7]))]

        weekend_avg_sales = weekend_sales.groupby('Store')['Sales'].mean().reset_index()
        logging.info("Weekend sales for stores open on weekdays:")
        logging.info(weekend_avg_sales)

        plt.figure(figsize=(12, 6))
        sns.barplot(x='Store', y='Sales', data=weekend_avg_sales, hue='Store', palette='coolwarm')
        plt.title("Average Weekend Sales for Weekday-Open Stores")
        plt.show()

    def assortment_type_effect(self):
        """Check how assortment type affects sales."""
        logging.info("Analyzing the effect of assortment type on sales.")
        assortment_sales = self.df.groupby('Assortment')['Sales'].mean().reset_index()

        plt.figure(figsize=(8, 5))
        sns.barplot(x='Assortment', y='Sales', data=assortment_sales, hue='Assortment', palette='coolwarm')
        plt.title("Effect of Assortment Type on Sales")
        plt.show()

    def competition_distance_effect(self):
        """Analyze how competition distance affects sales."""
        logging.info("Analyzing the effect of competition distance on sales.")
        sns.scatterplot(x='CompetitionDistance', y='Sales', data=self.df, alpha=0.6)
        plt.title("Effect of Competition Distance on Sales")
        plt.xlabel("Competition Distance")
        plt.ylabel("Sales")
        plt.show()

    def competitor_open_reopen_effect(self):
        """Analyze the impact of competitor openings or reopenings on sales."""
        logging.info("Analyzing the impact of competitor openings or reopenings on sales.")
        self.df['CompetitorOpen'] = pd.to_datetime(
            self.df['CompetitionOpenSinceYear'].fillna(0).astype(int).astype(str) + '-' +
            self.df['CompetitionOpenSinceMonth'].fillna(1).astype(int).astype(str) + '-01', errors='coerce'
        )
        self.df['MonthsSinceCompetition'] = ((self.df['Date'] - self.df['CompetitorOpen']).dt.days / 30).fillna(-1)

        sns.lineplot(x='MonthsSinceCompetition', y='Sales', data=self.df, errorbar=None)
        plt.title("Sales Impact by Months Since Competitor Open")
        plt.xlabel("Months Since Competition Opened")
        plt.ylabel("Sales")
        plt.show()

    def correlation_sales_customers(self):
        """Calculate and visualize the correlation between sales and customers."""
        logging.info("Calculating the correlation between sales and customers.")
        correlation = self.df[['Sales', 'Customers']].corr()
        logging.info("Correlation Between Sales and Customers:")
        logging.info(correlation)

        sns.heatmap(correlation, annot=True, cmap='coolwarm')
        plt.title("Correlation Between Sales and Customers")
        plt.show()

    def promo_effect_on_sales(self):
        """Analyze the effect of promos on sales."""
        logging.info("Analyzing the effect of promos on sales.")
        promo_sales = self.df.groupby('Promo')['Sales'].mean().reset_index()

        plt.figure(figsize=(8, 5))
        sns.barplot(x='Promo', y='Sales', data=promo_sales, hue='Promo', palette='viridis')
        plt.title("Effect of Promo on Sales")
        plt.show()
