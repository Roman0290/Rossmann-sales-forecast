import os
import matplotlib.pyplot as plt
import seaborn as sns
from logger import setup_logger

# Set up logger
logger = setup_logger("Visualization")

def ensure_directory_exists(directory_path):
    """
    Ensure the given directory exists. If not, create it.
    """
    os.makedirs(directory_path, exist_ok=True)

def plot_promo_distribution(df):
    """
    Plot promotion distribution.
    """
    logger.info("Plotting promotion distribution.")
    # Ensure output directory exists
    output_dir = "outputs/eda"
    ensure_directory_exists(output_dir)

    # Plot the data
    plt.figure(figsize=(8, 6))
    sns.countplot(x="Promo", data=df)
    plt.title("Promotion Distribution")
    plt.xlabel("Promo")
    plt.ylabel("Count")

    # Save the plot
    plot_path = os.path.join(output_dir, "promo_distribution.png")
    plt.savefig(plot_path)
    logger.info(f"Saved promo distribution plot to {plot_path}")
    plt.show()

def plot_sales_vs_customers(df):
    """
    Plot sales vs customers.
    """
    logger.info("Plotting sales vs customers scatter plot.")
    # Ensure output directory exists
    output_dir = "outputs/eda"
    ensure_directory_exists(output_dir)

    # Plot the data
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="Customers", y="Sales", data=df)
    plt.title("Sales vs Customers")
    plt.xlabel("Customers")
    plt.ylabel("Sales")

    # Save the plot
    plot_path = os.path.join(output_dir, "sales_vs_customers.png")
    plt.savefig(plot_path)
    logger.info(f"Saved sales vs customers plot to {plot_path}")
    plt.show()
