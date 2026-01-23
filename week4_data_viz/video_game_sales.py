import matplotlib.pyplot as plt # type: ignore
import pandas as pd
import os

# file paths
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "dataset", "vgsales.csv")

# loading the data
df = pd.read_csv(file_path)

# droping the rows that have empty or missing info in them
df.dropna(inplace=True)