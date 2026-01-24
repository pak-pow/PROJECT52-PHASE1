import matplotlib.pyplot as plt # type: ignore
import pandas as pd
import os

# load file
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "dataset", "vgsales.csv")
df = pd.read_csv(file_path)

# data cleaning
df.dropna(inplace=True)
df['Year'] = df['Year'].astype(int)

# data filtering
df_2008 = df[df['Year'] == 2008]