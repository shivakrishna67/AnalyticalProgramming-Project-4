class DataSummary:
    def __init__(self) -> None:
        pass

    def dataSummaryMod(api_endpoint):
        """
        Fetch data from the specified API endpoint and return a pandas DataFrame.

        Parameters:
        - api_endpoint (str): The API endpoint to fetch data from.

        Returns:
        - pd.DataFrame: The DataFrame containing the fetched data.
        """
        print("Data Summary Starts here")
        print("*******************************************************************")
        print("Importing packages/libraries")
        import pandas as pd
        from sodapy import Socrata
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns

        print("Fetching Data from API End Point Starts")
        # Fetching the data using the API endpoint
        client = Socrata("data.cityofnewyork.us", None)
        results = client.get(api_endpoint, limit=180030)
        print(
            """
        1.If we don't specify the limit, the API returns only 1000 observations\n
        2. Mentioned the limit based on the data description on the website\n
        3. Convert to pandas DataFrame as the API returns data in JSON format"""
        )
        print("Convert to pandas DataFrame as the API returns data in JSON format")
        data = pd.DataFrame.from_records(results)
        print("Fetching Data from API End Point Ends here")
        print("Displaying the data")
        print(data)
        print("Display the imported data types of all attributes")
        print(data.info())
        print(
            "Pandas has considered the datatypes of attributes as displayed above by default, we would be converting them as per requirement(int/float) in further analysis."
        )
        print("Data Sumamry Ends here")
        print("*******************************************************************")
