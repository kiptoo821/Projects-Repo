
import seaborn as sns
import matplotlib.pyplot as plt

class DataVisualizer:
    """
    A class for creating common data visualizations (Line Chart, Bar Chart, Histogram, and Pie Chart) 
    using Seaborn, optimized for pandas DataFrames.
    """

    @staticmethod
    def line_chart(data, x, y, title="Line Chart"):
        """
        Creates a line chart using Seaborn.

        Parameters:
            data (pd.DataFrame): DataFrame containing the data.
            x (str): Column name for the x-axis.
            y (str): Column name for the y-axis.
            title (str): Title of the chart. Default is "Line Chart".

        Returns:
            None
        """
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data, x=x, y=y, marker="o")
        plt.title(title)
        plt.grid(True)
        plt.show()

    @staticmethod
    def bar_chart(data, x, y, title="Bar Chart"):
        """
        Creates a bar chart using Seaborn.

        Parameters:
            data (pd.DataFrame): DataFrame containing the data.
            x (str): Column name for the categories (x-axis).
            y (str): Column name for the values (y-axis).
            title (str): Title of the chart. Default is "Bar Chart".

        Returns:
            None
        """
        plt.figure(figsize=(10, 6))
        sns.barplot(data=data, x=x, y=y, palette="muted")
        plt.title(title)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    @staticmethod
    def histogram(data, column, bins=10, title="Histogram"):
        """
        Creates a histogram using Seaborn.

        Parameters:
            data (pd.DataFrame): DataFrame containing the data.
            column (str): Column name to plot the histogram.
            bins (int): Number of bins. Default is 10.
            title (str): Title of the chart. Default is "Histogram".

        Returns:
            None
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(data=data, x=column, bins=bins, kde=True, color="green")
        plt.title(title)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    @staticmethod
    def pie_chart(data, column, title="Pie Chart"):
        """
        Creates a pie chart from a DataFrame column.

        Parameters:
            data (pd.DataFrame): DataFrame containing the data.
            column (str): Column name containing the categorical data.
            title (str): Title of the chart. Default is "Pie Chart".

        Returns:
            None
        """
        plt.figure(figsize=(8, 8))
        counts = data[column].value_counts()
        plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("tab10"))
        plt.title(title)
        plt.axis('equal')  # Ensures pie chart is a circle
        plt.show()
