import pandas as pd
import os

def load_data():
    # 1. Get the exact folder path where this script is physically sitting
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Safely attach the CSV filename to that exact folder path
    csv_path = os.path.join(current_dir, "app_data.csv")
    
    # 3. Read it using the absolute path!
    file = pd.read_csv(csv_path)

    print("\nFirst look at the dataset:")
    print("-" * 40)
    print(file.head())
    print("-" * 40)

    print(f"\nTotal rows: {len(file)}")
    print(f"Columns found: {list(file.columns)}")
    
if __name__ == "__main__":
    load_data()