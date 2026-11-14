import pandas as pd

# Load dataset
df = pd.read_csv("dataset/netflix_titles.csv")

print("Original Shape:", df.shape)

# ----------------------------
# Remove duplicates
# ----------------------------
df.drop_duplicates(inplace=True)

# ----------------------------
# Handle Missing Values
# ----------------------------

# Replace missing text values with 'Unknown'
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")

# Drop rows where important information is missing
df.dropna(subset=["date_added", "duration"], inplace=True)

# ----------------------------
# Convert date_added
# ----------------------------

# Convert date_added

df["date_added"] = df["date_added"].str.strip()

df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

df.dropna(subset=["date_added"], inplace=True)

# ----------------------------
# Create New Features
# ----------------------------

df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month
df["day_added"] = df["date_added"].dt.day

print("\nCleaned Shape:", df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ----------------------------
# Save cleaned dataset
# ----------------------------
df.to_csv("dataset/cleaned_netflix.csv", index=False)

print("\nCleaned dataset saved successfully!")