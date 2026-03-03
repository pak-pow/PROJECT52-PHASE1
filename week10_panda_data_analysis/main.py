import pandas as pd
import os
import sys

def load_data():
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
    pass

if __name__ == "__main__":
    app_df = load_data()
    print_statistic(app_df)