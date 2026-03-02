import pandas as pd
import os

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

if __name__ == "__main__":
    app_df = load_data()
    print_statistic(app_df)