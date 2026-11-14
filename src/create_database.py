import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_netflix.csv")

# Create SQLite database
conn = sqlite3.connect("netflix.db")

# Store dataframe as SQL table
df.to_sql("netflix", conn, if_exists="replace", index=False)

print("Database created successfully!")

conn.close()