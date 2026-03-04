import pandas as pd
import os
import sys

def load_data():
    # The code snippet `current_dir = os.path.dirname(os.path.abspath(__file))` is getting the
    # directory path of the current Python script file. It uses `os.path.abspath(__file__)` to get the
    # absolute path of the current script file and then `os.path.dirname()` to extract the directory
    # path from the absolute path.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "app_data.csv")
    
    # returns the dataframe so other functions can use it
    return pd.read_csv(csv_path)
    
    
def print_statistic(df):
    print("CORE STATISTIC")
    print("-" * 40)
    
    # calculating total revenue
    total_revenue = df['Revenue_USD'].sum()
    print(f"Total Revenue: ${total_revenue:,.2f}")
    
    # calculate the average of downloads
    avg_download = df['Downloads'].mean()
    print(f"Average Daily Downloads: {avg_download:.0f}")
    
    # find the highest peak of active user
    max_user = df['Active_Users'].max()
    print(f"Peak Active Users: {max_user}")
    
    # calculate Total Crash Reports
    total_crashes = df['Crash_Reports'].sum()
    print(f"Total App Crashes: {total_crashes}")
    print("-" * 40)

def filter_data(df):
    print("[DATA FILTERING]: ")
    print("-" * 40)
    
    # This code snippet is filtering the DataFrame `df` to find and display the rows where the
    # 'Crash_Reports' column has a value greater than 10.
    high_crash_days = df[df['Crash_Reports'] > 10]
    print("Days with > 10 crashes")
    print(high_crash_days[['Date', 'Crash_Reports']])
    print("-" * 40)
    
    # This line of code is filtering the DataFrame `df` to find the row(s) where the 'Revenue_USD'
    # column has the maximum value.
    best_revenue_day = df[df['Revenue_USD'] == df['Revenue_USD'].max()]
    print("Best Revenue Day:")
    print(best_revenue_day[['Date', 'Revenue_USD']])
    print("-" * 40)
    
def group_data(df): 
    
    print("[DATA GROUPING (Pivot Tables)]:")
    print("-" * 40)
    
    # `platform_revenue = df.groupby('Platform')['Revenue_USD'].sum()` is grouping the data in the
    # DataFrame `df` by the 'Platform' column. It then calculates the sum of the 'Revenue_USD' column
    # for each unique value in the 'Platform' column. The result is a Series where the index is the
    # unique values in the 'Platform' column and the values are the total revenue (sum of
    # 'Revenue_USD') for each platform.
    platform_revenue = df.groupby('Platform')['Revenue_USD'].sum()
    
    # The code snippet `print("[Total Revenue By Platform]: ")` is printing a header or title
    # indicating that the following output will display the total revenue by platform.
    print("[Total Revenue By Platform]: ")
    print(platform_revenue)
    
    # `platform_crashes = df.groupby('Platform')['Crash_Reports'].mean()` is grouping the data in the DataFrame `df` by the 'Platform' column. It then calculates the mean (average) of the 'Crash_Reports' column for each unique value in the 'Platform' column. 
    # The result is a Series where the index is the unique values in the 'Platform' column and the values are the average number of crash reports for each platform.
    platform_crashes = df.groupby('Platform')['Crash_Reports'].mean()
    print(platform_crashes)
    print('-' * 40)

if __name__ == "__main__":
    # The code snippet `app_df = load_data()` loads data from a CSV file into a pandas DataFrame and
    # assigns it to the variable `app_df`.
    app_df = load_data()
    # filter_data(app_df)
    group_data(app_df)