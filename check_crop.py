import pandas as pd

df = pd.read_csv("dataset/crop_data.csv")

print(sorted(df["Crop"].unique()))