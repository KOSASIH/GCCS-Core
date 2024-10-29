# src/utils/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class DataVisualizer:
    """Class for visualizing data."""

    def __init__(self):
        sns.set(style="whitegrid")

    def plot_time_series(self, data, x_col, y_col, title='Time Series Plot'):
        """Plot a time series graph."""
        plt.figure(figsize=(12, 6))
        plt.plot(data[x_col], data[y_col], marker='o')
        plt.title(title)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_correlation_matrix(self, data, title='Correlation Matrix'):
        """Plot a heatmap of the correlation matrix."""
        plt.figure(figsize=(10, 8))
        correlation = data.corr()
        sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm', square=True)
        plt.title(title)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example usage
    df = pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', periods=10),
        'temperature': [20, 21, 19, 22, 23, 24, 25, 26, 27, 28],
        'humidity': [30, 32, 31, 29, 28, 27, 26, 25, 24, 23]
    })
    df.set_index('date', inplace=True)

    visualizer = DataVisualizer()
    visualizer.plot_time_series(df, x_col='date', y_col='temperature', title='Temperature Over Time')
    visualizer.plot_correlation_matrix(df, title='Correlation Matrix of Weather Data')
