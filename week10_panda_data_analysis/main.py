import pandas as pd

def load_data():
    
    file = pd.read_csv("app_data.csv")

    print("\n📊 First look at the dataset:")
    print("-" * 40)
    print(file.head())
    print("-" * 40)

    print(f"\nTotal rows: {len(file)}")
    print(f"Columns found: {list(file.columns)}")
    
    pass

if __name__ == "__main__":
    load_data()