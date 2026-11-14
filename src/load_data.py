import pandas as pd

# Load the dataset
df = pd.read_csv("dataset/netflix_titles.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Shape of dataset
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns.tolist())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe(include='all'))

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())