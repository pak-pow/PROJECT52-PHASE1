import pandas as pd
import os

def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "app_data.csv")
    
    return pd.read_csv(csv_path)
    
if __name__ == "__main__":
    load_data()