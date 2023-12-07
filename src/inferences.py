class Inference:
    def __init__(self) -> None:
        pass

    def inferences(data):
        """
        Performs inferences based on the provided data and prints the results.

        Args:
            data (pd.DataFrame): The pandas DataFrame containing the exploratory data analysis results.

        Returns:
            None
        """
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns

        print("""Inferences Starts here.....""")
        print(
            """Now that we've completed the Exploratory Data Analysis we'll perform the analysis required to answer the research question. For any visualizations necessary, I will create the graphic using both Matplotlib and Seaborn."""
        )
        print(
            """*********************************************************************
    Inference 1 : What are the temporal trends in motor vehicle crashes over time? Are there specific times of the day, days of the week, or months with higher accident rates?
    ******************************************************************************
    """
        )
        # crashes by month
        print("crashes by month")
        print(data["Month"].value_counts())
        # bar plot for Month with matplot lib
        # Plotting with Matplotlib
        month_bar_plot_matplotlib = (
            data["Month"].value_counts().sort_values().plot(kind="bar")
        )
        month_bar_plot_matplotlib.set_title("MATPLOTLIB: Number of Crashes per Month")
        month_bar_plot_matplotlib.set_xticklabels(
            month_bar_plot_matplotlib.get_xticklabels(), rotation=45
        )

        # Display the Matplotlib plot
        plt.show()

        # Plotting with Seaborn
        month_bar_plot_seaborn = sns.countplot(x="Month", data=data)
        month_bar_plot_seaborn.set_title("SEABORN: Number of Crashes per Month")
        month_bar_plot_seaborn.set_xticklabels(
            month_bar_plot_seaborn.get_xticklabels(), rotation=45
        )
        # Display the Seaborn plot
        plt.show()
        print("Crashes By Day")
        # crashes by day
        print(data["Day"].value_counts())
        # bar plot for day with matplot lib
        plt.figure(figsize=(13, 5))
        plt.subplot(1, 2, 1)
        day_bar_plot = data["Day"].value_counts().plot(kind="bar")
        # set the title of the bar plot
        day_bar_plot.set_title("MATPLOTLIB: Number of Crashes per Day")
        day_bar_plot.set_xticklabels(day_bar_plot.get_xticklabels(), rotation=45)
        # show the plot
        plt.show()

        plt.subplot(1, 2, 1)
        # Now I will create the same bar plot but using Seaborn
        # Seaborn has a built in countplot function that does the counting and plot the data
        day_bar_plot = sns.countplot(x="Day", data=data)
        day_bar_plot.set_title("SEABORN: Number of Crashes per Day")
        # show the bar/count plot
        plt.show()
        day_bar_plot

        print("Crashes by the time of the day")
        print(data["crash_time"].value_counts())

        # as we have crash time first we convert into a integer so that it will get round of to the hour
        data["crash_time"] = data["crash_time"].str.split(":", expand=True)[0]
        plt.figure(figsize=(13, 5))
        plt.subplot(1, 2, 1)
        # Matplotlib bar plot for the Number of Crashes by hour of day
        hour = data["crash_time"].value_counts().head().plot(kind="bar")
        hour.set_title("MATPLOTLIB: Number of Crashes by hour of day")
        hour.set_xticklabels(hour.get_xticklabels(), rotation=0)
        plt.show()

        plt.subplot(1, 2, 2)
        # Seaboarn bar plot for the Number of Crashes by hour of the day
        hour = data["crash_time"].value_counts().head()
        hour = sns.barplot(x=hour.index, y=hour.values)
        hour.set_title("SEABORN: Number of Crashes by hpour of day")
        plt.show()
        hour
        print(
            """
    From the EDA I can conclude that, More number of crashes has occured in the months of May, 
    June and July. To be specific all the months in first 3 quaters have more no of crashes with 
    less varying in number, but the months of last quarter that is October, November and December 
    having a very less number of crashes. So we can observe a strong seasonality across the months
    of a year. In the similar way we can see very little seasonilty across the days of the week, 
    Tuesday and wednesday has he highest number of crashes, even they vary with very lesser number
      of crashes.And we have more crashes from 2pm to 6pm"""
        )

        print(
            """**********************************************************************
    Inference 2 : Is there a correlation between the time of day and the severity of crashes (i.e., more fatalities during certain hours)?
    *****************************************************************************"""
        )
        # as we have crash time first we convert into a integer so that it will get round of to the hour
        data["crash_time"] = data["crash_time"].str.split(":", expand=True)[0]
        plt.figure(figsize=(13, 5))
        plt.subplot(1, 2, 1)
        # Matplotlib bar plot for the Number of Crashes by hour of day
        hour = data["crash_time"].value_counts().head().plot(kind="bar")
        hour.set_title("MATPLOTLIB: Number of Crashes by hour of day")
        hour.set_xticklabels(hour.get_xticklabels(), rotation=0)
        plt.show()

        plt.subplot(1, 2, 2)
        # Seaboarn bar plot for the Number of Crashes by hour of the day
        hour = data["crash_time"].value_counts().head()
        hour = sns.barplot(x=hour.index, y=hour.values)
        hour.set_title("SEABORN: Number of Crashes by hpour of day")
        hour
        plt.show()
        print(
            """Interesting there is a strong relation between the time of the day and the crashes. From EDA I found that mostly crashes has been happened only from 2pm to 7pm."""
        )

        print(
            """*****************************************************************************
    Inference 3 : Where are the most dangerous locations for motor vehicle crashes? Can we identify high-risk areas?
    ************************************************************************************"""
        )
        plt.figure(figsize=(13, 5))
        plt.subplot(1, 2, 1)
        # Matplotlib bar plot for the Number of Crashes by Borough
        # plt.gcf().set_size_inches(8, 5)
        borough = data["borough"].value_counts().plot(kind="bar")
        borough.set_title("MATPLOTLIB: Number of Crashes by Borough")
        borough.set_xticklabels(borough.get_xticklabels(), rotation=45)
        plt.show()

        plt.subplot(1, 2, 2)
        # plt.gcf().set_size_inches(10, 15)
        # Seaboarn bar plot for the Number of Crashes by Borough
        borough = sns.countplot(y="borough", data=data)
        borough.set_title("SEABORN: Number of Crashes by Borough")
        borough
        plt.show()

        print(
            """************************************************************
    Inference 4 : Are there seasonal variations in the frequency and severity of motor vehicle crashes?
    **********************************************************************"""
        )
        print(
            """There is a strong seasonality across the particular time of the day which is from 2pm to 7pm and among the months its first 3 quaters has large number of crashes with less varying number of crashes across the months of first 3 quaters."""
        )
