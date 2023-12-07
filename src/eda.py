class EDA:
    def __init__(self) -> None:
        pass

    def exploratoryDataAnalysis():
        """
        Performs exploratory data analysis (EDA) on a dataset related to vehicle crashes in New York City.

        This EDA includes the following steps:
        1. Data Loading: Fetches data from the NYC Open Data API using the Socrata library.
        2. Data Cleaning: Drops unnecessary attributes/columns from the dataset.
        3. Null Value Check: Identifies and prints the number of null values in the dataset.
        4. Summary Statistics: Displays summary statistics for numerical columns in the dataset.
        5. Attribute Analysis: Provides detailed analysis for specific attributes such as crash date, time, borough, and street.
        6. Time Analysis: Explores patterns in crashes over the years, months, and days of the week.
        7. Visualizations: Utilizes both Matplotlib and Seaborn for visualizing the dataset, including bar plots and histograms.
        8. Additional Analyses: Investigates the number of injuries and deaths, their distribution over months and days, and their correlation.
        9. Contributing Factors: Examines contributing factors to crashes and their impact on injuries and deaths.
        10. Comparative Analysis: Compares the number of injuries and deaths using a scatter plot.

        Note: The code assumes the presence of the 'Socrata' library for data fetching and requires a specific API endpoint for NYC crash data.

        Returns:
        - pandas DataFrame: The cleaned and analyzed dataset after performing the exploratory data analysis.
        """
        print("*******************************************************")
        print("EDA Starts here")
        print(
            """In order to go on with this portion of the study, we will first run a summary statistic for each of the characteristics, look for any outliers or NULL values that could have an impact on our findings, and then provide graphical analyses for each attribute using both Matplotlib and Seaborn.\n
                To begin, we'll import the required packages/libraries and then read the data into the program as shown"""
        )
        # Import packages/libraries
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns
        from sodapy import Socrata

        # Fetching the data using the API endpoint
        client = Socrata("data.cityofnewyork.us", None)
        results = client.get("h9gi-nx95", limit=180030)
        # if we dont specify the limit API returns only 1000 observations,so I came to know that there are 180030 observation from the data description given in the webiste so mentioned the limit
        # Convert to pandas DataFrame as API returns data in JSON format
        data = pd.DataFrame.from_records(results)
        # lets drop the attributes that we are not considering to answer the above mentioned research
        print(
            "lets drop the attributes that we are not considering to answer the above mentioned research"
        )
        print(
            "============================================================================================="
        )
        data = data.drop(
            [
                "zip_code",
                "latitude",
                "longitude",
                "location",
                "cross_street_name",
                "off_street_name",
                "contributing_factor_vehicle_2",
                "contributing_factor_vehicle_3",
                "contributing_factor_vehicle_4",
                "contributing_factor_vehicle_5",
                "vehicle_type_code2",
                "vehicle_type_code_3",
                "vehicle_type_code_4",
                "vehicle_type_code_5",
            ],
            axis=1,
        )
        print("Data after dropping the unwanted attributes")
        print(
            "============================================================================================="
        )
        print(data)
        print(
            "*********************************************************************************************"
        )
        print(
            """Since we've successfully imported the data, we'll proceed to look through the data if there are null values. Null values may impact our research so we'll have to be keen"""
        )
        # Looking for the number of null values
        print("Looking for the number of null values")
        print(data.isnull().sum())
        print(
            "From the above analysis we can see that there were null values only in 4 columns namely on_street_name, contributing_factor_vehicle_1 , vehicle_type_code1 and borough."
        )
        # sumamry statistics of the data
        print(
            """========================================================
                        sumamry statistics of the data
                        ========================================================="""
        )
        print(data.describe())
        print(
            "Observations : From the above statistics we can observe the median mode and mean values for all numerical columns and understand the distribution of the data"
        )
        print(
            """===========================================================
                        Now lets analyse the each attribute
                        ========================================================="""
        )
        print(
            """*********************************************************
                        Crash Date 
                        *********************************************************"""
        )
        print(data["crash_date"].describe())
        print(
            """From the above data it is found that there are 814 unique values in the crash date attribute."""
        )
        print(
            """*********************************************************
                        Crash Time 
                        *********************************************************"""
        )
        print(data["crash_time"].describe())
        print(
            "from the above data it is found that there are 1440 unique values in the crash time attribute."
        )
        print(
            """*********************************************************
                        Borough 
                        *********************************************************"""
        )
        print(data["borough"].describe())

        # Using Seaborn
        print("Using Seaborn")
        plt.figure(figsize=(13, 5))
        plt.subplot(1, 2, 1)
        sns.countplot(x=data["borough"], palette="viridis")
        plt.title("Seaborn Countplot - borough")
        plt.xlabel("borough")
        plt.ylabel("Count")
        # Using Matplotlib
        print("Using Matplotlib")
        plt.subplot(1, 2, 2)
        value_counts = data["borough"].value_counts()
        plt.bar(value_counts.index, value_counts, color="skyblue")
        plt.title("Matplotlib Countplot - borough")
        plt.xlabel("borough")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()
        print(
            "From the above data it is found that there are 5 unique values in the Borough attribute.Which says that there are 5 different borough are present."
        )
        # On Street Name
        print(
            """*********************************************************
                        On Street name 
                        *********************************************************"""
        )
        print(data["on_street_name"].describe())
        print(
            "From the above data it is found that there are 7727 unique streets involved in crash in New York City."
        )
        print(
            """*********************************************************
                        Number of persons Injured
                        *********************************************************"""
        )
        data["number_of_persons_injured"] = data["number_of_persons_injured"].astype(
            int
        )
        print(data["number_of_persons_injured"].describe())
        # Using Seaborn
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        sns.histplot(data["number_of_persons_injured"], kde=True, color="skyblue")
        plt.title("Seaborn Histogram - number_of_persons_injured")
        plt.xlabel("number_of_persons_injured")
        plt.ylabel("Frequency")
        # Using Matplotlib
        plt.subplot(1, 2, 2)
        plt.hist(
            data["number_of_persons_injured"],
            bins=10,
            color="salmon",
            edgecolor="black",
        )
        plt.title("Matplotlib Histogram - number_of_persons_injured")
        plt.xlabel("number_of_persons_injured")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()
        print(
            """We have total 180030 observations and from the above statistical data we can observe that the average no of persons injured in the crashes is 1 person per two crashes.From the above distribution, we can say that mostly number of persons injured were falling in the bin of 0 - 5. 
                """
        )

        print(
            """*********************************************************
                        Number of persons Killed
                        *********************************************************"""
        )
        data["number_of_persons_killed"] = data["number_of_persons_killed"].astype(int)
        # here we can find the average and std deviation min and max no of people can be killed per a crash as below
        print(
            "here we can find the average and std deviation min and max no of people can be killed per a crash as below"
        )
        print(data["number_of_persons_killed"].describe())

        # Using Seaborn
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        sns.histplot(data["number_of_persons_killed"], kde=True, color="skyblue")
        plt.title("Seaborn Histogram - number_of_persons_killed")
        plt.xlabel("number_of_persons_killed")
        plt.ylabel("Frequency")

        # Using Matplotlib
        plt.subplot(1, 2, 2)
        plt.hist(
            data["number_of_persons_killed"], bins=10, color="salmon", edgecolor="black"
        )
        plt.title("Matplotlib Histogram - number_of_persons_killed")
        plt.xlabel("number_of_persons_killed")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()
        print(
            "From the above distribution we can say that the maximum number of people killed per crash is 3 people."
        )

        # now lets convert the Crash date into a date data type
        data["crash_date"] = pd.to_datetime(data["crash_date"])
        print("Below are the data types for all attributes")
        print(data.dtypes)
        print(
            """In the below step we extract the day month and year from the crash date attribute and also changed to its respective month day names to make easier to analyse the data well."""
        )

        import calendar

        # Exctracting the year, month, day to analyse the seasonal and temporal time analysis of crashes
        print(
            "Exctracting the year, month, day to analyse the seasonal and temporal time analysis of crashes"
        )
        data["Day"] = data["crash_date"].dt.day
        data["Month"] = data["crash_date"].dt.month
        data["Year"] = data["crash_date"].dt.year
        # Map month and day numbers to their names without using map
        data["Month"] = [calendar.month_name[x] for x in data["Month"]]
        data["Day"] = [
            calendar.day_name[x % 7] for x in data["Day"]
        ]  # % 7 to handle Sunday as the first day
        print("Displaying the data")
        print(data)
        print(
            """************************************************
                        EDA - No of Crashes by Year
                        ************************************************"""
        )
        print(
            """First I will get summary statistics on the attribute Year. Then, since Year is an ordinal variable, I will generate bar plots using both Matplotlib and Seaborn."""
        )
        # bar plot for year with matplotlib
        year_bar_plot = data["Year"].value_counts().sort_index().plot(kind="bar")
        # set the title of the bar plot
        year_bar_plot.set_title("MATPLOTLIB: Number of Crashes per Year")
        year_bar_plot.set_xticklabels(year_bar_plot.get_xticklabels(), rotation=45)
        # show the plot
        plt.show()
        # Now I will create the same bar plot but using Seaborn
        # Seaborn has a built in countplot function that does the counting and plot the data
        year_bar_plot = sns.countplot(x="Year", data=data)
        year_bar_plot.set_title("SEABORN: Number of Crashes per Year")
        # show the bar/count plot
        year_bar_plot
        plt.show()
        print(
            "From the above graphs it was evident that a large no of crashes happened during 2021."
        )
        print(
            """**************************************************
                        EDA - No of crashes by Month
                        **************************************************"""
        )
        # bar plot for Month with matplot lib
        month_bar_plot = data["Month"].value_counts().sort_values().plot(kind="bar")
        # set the title of the bar plot
        month_bar_plot.set_title("MATPLOTLIB: Number of Crashes per Month")
        month_bar_plot.set_xticklabels(month_bar_plot.get_xticklabels(), rotation=45)
        # show the plot
        plt.show()

        # Now I will create the same bar plot but using Seaborn
        # Seaborn has a built in countplot function that does the counting and plot the data
        month_bar_plot = sns.countplot(x="Month", data=data)
        month_bar_plot.set_title("SEABORN: Number of Crashes per Month")
        month_bar_plot.set_xticklabels(month_bar_plot.get_xticklabels(), rotation=45)
        # show the bar/count plot
        print("month_bar_plot")
        plt.show()
        print(
            "As per the above plots it was evident that June marks the highest and then followed by May . To be specific Quarter 4 has the least no of crashes.The reason behind this may be that as it was a winter season people are less tend to travel leading to less no of crashes."
        )

        print(
            """*************************************************************
                        EDA - Crashes by Day
                        ************************************************************"""
        )
        plt.figure(figsize=(13, 5))
        plt.subplot(1, 2, 1)
        # bar plot for day with matplot lib
        day_bar_plot = data["Day"].value_counts().plot(kind="bar")
        # set the title of the bar plot
        day_bar_plot.set_title("MATPLOTLIB: Number of Crashes per Day")
        day_bar_plot.set_xticklabels(day_bar_plot.get_xticklabels(), rotation=45)
        # show the plot
        plt.show()

        plt.subplot(1, 2, 2)
        # Now I will create the same bar plot but using Seaborn
        # Seaborn has a built in countplot function that does the counting and plot the data
        day_bar_plot = sns.countplot(x="Day", data=data)
        day_bar_plot.set_title("SEABORN: Number of Crashes per Day")
        # show the bar/count plot
        plt.show()
        print(
            "From the above plots It is evident that Tuesday marks the highest crashes day followed by wednesday and Thursday with slight difference."
        )

        print(
            """********************************************************
                        EDA - Crashes by Borough
                        ******************************************************"""
        )
        # Matplotlib bar plot for the Number of Crashes by Borough
        # plt.gcf().set_size_inches(8, 5)
        plt.figure(figsize=(13, 5))
        plt.subplot(1, 2, 1)
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
            "Based on the data shown above, it is obvious that Brooklyn stood at first place for happening most crashes followed by Queens and STATEN ISLAND beinhg the least and indicating the safe place in terms of travelling."
        )

        print(
            """*****************************************************
                        EDA - Crashes by Street
                        *****************************************************"""
        )
        # Matplotlib bar plot for the Number of Crashes by Street
        plt.figure(figsize=(13, 5))
        plt.subplot(1, 2, 1)
        street = data["on_street_name"].value_counts().head().plot(kind="bar")
        street.set_title("MATPLOTLIB: Number of Crashes by Street")
        street.set_xticklabels(street.get_xticklabels(), rotation=45)
        plt.show()

        plt.subplot(1, 2, 2)
        # Seaboarn bar plot for the Number of Crashes by Street
        streets = data["on_street_name"].value_counts().head(5)
        streeti = sns.barplot(x=streets.index, y=streets.values)
        streeti.set_title("SEABORN: Number of Crashes by Street")
        streeti.set_xticklabels(streeti.get_xticklabels(), rotation=45)
        plt.show()
        print(
            "As there were very large number of street Here I displayed only top 5 streets of having large number of crashes.Belt parkway experience the most no of vehicle crashes follwed by long island express highway."
        )

        print(
            """****************************************************
                        EDA - No of Injuries by Month and Day
                        ***************************************************"""
        )
        # converting the string to integer data type for the column number of persons injured
        data["number_of_persons_injured"] = data["number_of_persons_injured"].astype(
            int
        )
        monthly_injuries = (
            data.groupby("Month")["number_of_persons_injured"].sum().reset_index()
        )

        # Create the bar plot using seaborn
        plt.figure(figsize=(15, 6))
        plt.subplot(1, 2, 1)
        sns.barplot(x="Month", y="number_of_persons_injured", data=monthly_injuries)
        plt.title("Number of Injuries by Month")
        plt.xlabel("Month")
        plt.ylabel("Total Injuries")
        plt.show()

        plt.subplot(1, 2, 2)
        # using matplotlib
        plt.bar(
            monthly_injuries["Month"], monthly_injuries["number_of_persons_injured"]
        )
        plt.title("Number of Injuries by Month")
        plt.xlabel("Month")
        plt.ylabel("Total Injuries")
        plt.show()
        print("June and July months experience the most number of people got injured")

        print(
            """********************************************************************
                        EDA - Deaths by Day
                        ********************************************************************"""
        )
        day_injuries = (
            data.groupby("Day")["number_of_persons_injured"].sum().reset_index()
        )

        plt.figure(figsize=(15, 6))
        plt.subplot(1, 2, 1)
        # Create the bar plot using seaborn
        sns.barplot(x="Day", y="number_of_persons_injured", data=day_injuries)
        plt.title("Number of Injuries by Month")
        plt.xlabel("Day")
        plt.ylabel("Total Injuries")
        plt.show()

        plt.subplot(1, 2, 2)
        # using matplotlib
        plt.figure(figsize=(15, 6))  # Set the figure size
        plt.bar(day_injuries["Day"], day_injuries["number_of_persons_injured"])
        plt.title("Number of Injuries by Day")
        plt.xlabel("MoDaynth")
        plt.ylabel("Total Injuries")
        plt.show()
        print(
            "From the above plots Tuesday and Wednesday has the highest no of injuries in a week but all are having slight difference."
        )

        print(
            """*********************************************************************
                EDA - Deaths by Month and Day
                **************************************************************************"""
        )
        data["number_of_persons_killed"] = data["number_of_persons_killed"].astype(int)
        monthly_deaths = (
            data.groupby("Month")["number_of_persons_killed"].sum().reset_index()
        )
        # Create the bar plot using seaborn

        plt.figure(figsize=(15, 6))
        plt.subplot(1, 2, 1)
        sns.barplot(x="Month", y="number_of_persons_killed", data=monthly_deaths)
        plt.title("Number of Deaths by Month")
        plt.xlabel("Month")
        plt.ylabel("Total Deaths")
        plt.show()

        # using matplotlib
        plt.subplot(1, 2, 2)
        plt.bar(monthly_deaths["Month"], monthly_deaths["number_of_persons_killed"])
        plt.title("Number of Deaths by Month")
        plt.xlabel("Month")
        plt.ylabel("Total Deaths")
        plt.show()
        print(
            "As earlier July has most no of deaths and the months of last quarter i.e.,October, November and December and september also stood at least no of deaths."
        )

        plt.figure(figsize=(15, 6))
        plt.subplot(1, 2, 1)
        day_deaths = data.groupby("Day")["number_of_persons_killed"].sum().reset_index()

        # Create the bar plot using seaborn
        sns.barplot(x="Day", y="number_of_persons_killed", data=day_deaths)
        plt.title("Number of Deaths by Day")
        plt.xlabel("Day")
        plt.ylabel("Total Deaths")
        plt.show()

        plt.subplot(1, 2, 1)
        # using matplotlib
        plt.figure(figsize=(10, 6))  # Set the figure size
        plt.bar(day_deaths["Day"], day_deaths["number_of_persons_killed"])
        plt.title("Number of deaths by Day")
        plt.xlabel("Day")
        plt.ylabel("Total Deaths")
        plt.show()
        print(
            "From the above plots, it is evident that weekdays Thursday has highest number of deaths followed by the Tuesday."
        )

        print(
            """"************************************************************
                        EDA - Cause of the Crash
                        **********************************************************"""
        )
        # Matplotlib bar plot for the Number of Crashes by Cause of crash
        plt.figure(figsize=(15, 6))
        plt.subplot(1, 2, 1)
        cause = (
            data["contributing_factor_vehicle_1"].value_counts().head().plot(kind="bar")
        )
        cause.set_title("MATPLOTLIB: Number of Crashes by cause of crash")
        cause.set_xticklabels(cause.get_xticklabels(), rotation=45)
        plt.show()

        plt.subplot(1, 2, 2)
        # Seaboarn bar plot for the Number of Crashes by Borough
        cause = data["contributing_factor_vehicle_1"].value_counts().head()
        cause = sns.barplot(x=cause.index, y=cause.values)
        cause.set_title("SEABORN: Number of Crashes by cause of crash")
        cause.set_xticklabels(cause.get_xticklabels(), rotation=45)
        cause
        plt.show()
        print(
            "As there are large number of causes and unable to read from a messy visual I have shown top 5 causes in the plot.Driver Inattention/ Distraction is the main reason for the crashes if we set aside the unspecified reason."
        )

        print(
            """********************************************************
                EDA - Crashes by Time of the day
                **********************************************************"""
        )
        # as we have crash time first we convert into a integer so that it will get round of to the hour
        data["crash_time"] = data["crash_time"].str.split(":", expand=True)[0]
        plt.figure(figsize=(15, 6))
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
            "From the above plot it is very interesting to observe that all the crashes has happened from 2pm to 6pm ."
        )

        print(
            """****************************************************
                EDA -Deaths by Borough
                *******************************************************"""
        )

        # Calculate the total sum of people killed in each borough
        borough_totals = (
            data.groupby("borough")["number_of_persons_killed"].sum().reset_index()
        )

        plt.figure(figsize=(15, 6))
        plt.subplot(1, 2, 1)
        # Create a bar plot with Seaborn
        plt.figure(figsize=(10, 6))
        sns.barplot(
            x="borough",
            y="number_of_persons_killed",
            data=borough_totals,
            palette="viridis",
        )
        plt.title("No of People Killed by Borough")
        plt.xlabel("Borough")
        plt.ylabel("No of People Killed")
        plt.show()
        plt.subplot(1, 2, 2)
        # Create a bar plot with Matplotlib
        plt.figure(figsize=(10, 6))
        plt.bar(
            borough_totals["borough"],
            borough_totals["number_of_persons_killed"],
            color="skyblue",
        )
        plt.title("No of People Killed by Borough")
        plt.xlabel("Borough")
        plt.ylabel("No of People Killed")
        plt.xticks(rotation=45, ha="right")
        plt.show()
        print(
            "Brooklyn has more number of deaths followed by the Bronx.Staten Island is the borough with the least number of deaths."
        )

        print(
            """************************************************************************
                EDA - Deaths by Cause
                *******************************************************************************"""
        )
        # Calculate the total sum of people killed in each borough
        borough_totals = (
            data.groupby("contributing_factor_vehicle_1")["number_of_persons_killed"]
            .sum()
            .reset_index()
            .head()
        )

        # Create a bar plot with Seaborn
        plt.figure(figsize=(10, 6))
        plt.subplot(1, 2, 1)
        sns.barplot(
            x="contributing_factor_vehicle_1",
            y="number_of_persons_killed",
            data=borough_totals,
            palette="viridis",
        )
        plt.title("No of People Killed by contributing factor")
        plt.xlabel("Contributing factor")
        plt.ylabel("No of People Killed")
        plt.show()

        plt.subplot(1, 2, 2)
        # Create a bar plot with Matplotlib
        plt.bar(
            borough_totals["contributing_factor_vehicle_1"],
            borough_totals["number_of_persons_killed"],
            color="skyblue",
        )
        plt.title("No of People Killed by contributing factor")
        plt.xlabel("Contributing factor")
        plt.ylabel("No of People Killed")
        plt.xticks(rotation=45, ha="right")
        plt.show()
        print(
            "More number of people were killed because of the Alcohol involvement followed by the Aggressive driving."
        )
        print(
            """**********************************************************************
                Injuries v/s Deaths
                *************************************************************************"""
        )

        # Create a scatter plot with Matplotlib
        plt.figure(figsize=(8, 6))
        plt.scatter(
            data["number_of_persons_killed"].astype(int),
            data["number_of_persons_injured"].astype(int),
            color="coral",
        )
        plt.title("Scatter Plot: Number of Deaths vs. Number of Injuries")
        plt.xlabel("Number of Deaths")
        plt.ylabel("Number of Injuries")
        plt.grid(True)
        plt.show()
        print("EDA Ends here")
        data["borough"].fillna("BROOKLYN", inplace=True)
        data["borough"] = data["borough"].map(
            {"BROOKLYN": 0, "QUEENS": 1, "BRONX": 2, "MANHATTAN": 3, "STATEN ISLAND": 4}
        )
        data["Day"] = data["Day"].map(
            {
                "Sunday": 0,
                "Monday": 1,
                "Tuesday": 2,
                "Wednesday": 3,
                "Thursday": 4,
                "Friday": 5,
                "Saturday": 6,
            }
        )
        data["Month"] = data["Month"].map(
            {
                "January": 0,
                "February": 1,
                "March": 2,
                "April": 3,
                "May": 4,
                "June": 5,
                "July": 6,
                "August": 7,
                "September": 8,
                "October": 9,
                "November": 10,
                "December": 11,
            }
        )
        for col in data.columns:
            if col == "crash_time" or col == "crash_date":
                continue
            data[col] = data[col].astype(int)
        return data
