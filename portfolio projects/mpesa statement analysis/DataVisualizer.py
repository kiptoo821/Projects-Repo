
import matplotlib.pyplot as plt

class DataVisualizer:
    """
    A class for creating common data visualizations: Line Chart, Bar Chart, Histogram, and Pie Chart.
    """

    @staticmethod
    def line_chart(x, y, title="Line Chart", xlabel="X-axis", ylabel="Y-axis"):
        """
        Creates a line chart.

        Parameters:
            x (list): Data for the x-axis.
            y (list): Data for the y-axis.
            title (str): Title of the chart. Default is "Line Chart".
            xlabel (str): Label for the x-axis. Default is "X-axis".
            ylabel (str): Label for the y-axis. Default is "Y-axis".

        Returns:
            None
        """
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, marker='o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()

    @staticmethod
    def bar_chart(categories, values, title="Bar Chart", xlabel="Categories", ylabel="Values"):
        """
        Creates a bar chart.

        Parameters:
            categories (list): Labels for each bar.
            values (list): Heights of each bar.
            title (str): Title of the chart. Default is "Bar Chart".
            xlabel (str): Label for the x-axis. Default is "Categories".
            ylabel (str): Label for the y-axis. Default is "Values".

        Returns:
            None
        """
        plt.figure(figsize=(8, 6))
        plt.bar(categories, values, color='skyblue', edgecolor='black')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    @staticmethod
    def histogram(data, bins=10, title="Histogram", xlabel="Bins", ylabel="Frequency"):
        """
        Creates a histogram.

        Parameters:
            data (list): Data to be distributed into bins.
            bins (int): Number of bins. Default is 10.
            title (str): Title of the chart. Default is "Histogram".
            xlabel (str): Label for the x-axis. Default is "Bins".
            ylabel (str): Label for the y-axis. Default is "Frequency".

        Returns:
            None
        """
        plt.figure(figsize=(8, 6))
        plt.hist(data, bins=bins, color='lightgreen', edgecolor='black', alpha=0.7)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    @staticmethod
    def pie_chart(labels, values, title="Pie Chart"):
        """
        Creates a pie chart.

        Parameters:
            labels (list): Labels for each segment of the pie.
            values (list): Values corresponding to each segment.
            title (str): Title of the chart. Default is "Pie Chart".

        Returns:
            None
        """
        plt.figure(figsize=(8, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)
        plt.title(title)
        plt.axis('equal')  # Ensures pie chart is a circle
        plt.show()
