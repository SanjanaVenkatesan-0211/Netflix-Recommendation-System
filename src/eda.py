import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images folder if it doesn't exist
# os.makedirs("images", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_netflix.csv")

plt.figure(figsize=(6,5))

sns.countplot(data=df, x="type")

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")

plt.savefig("images/movies_vs_tvshows.png")

plt.show()


plt.figure(figsize=(10,6))

sns.countplot(
    data=df,
    y="rating",
    order=df["rating"].value_counts().index
)

plt.title("Content Ratings on Netflix")

plt.savefig("images/content_ratings.png")

plt.show()


country_counts = (
    df["country"]
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10,6))

sns.barplot(
    x=country_counts.values,
    y=country_counts.index
)

plt.title("Top 10 Content Producing Countries")

plt.xlabel("Number of Titles")

plt.savefig("images/top_countries.png")

plt.show()


genre_counts = (
    df["listed_in"]
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10,6))

sns.barplot(
    x=genre_counts.values,
    y=genre_counts.index
)

plt.title("Top 10 Netflix Genres")

plt.xlabel("Number of Titles")

plt.savefig("images/top_genres.png")

plt.show()


year_counts = (
    df["year_added"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(12,6))

plt.plot(
    year_counts.index,
    year_counts.values,
    marker="o"
)

plt.title("Netflix Content Added Over the Years")

plt.xlabel("Year")

plt.ylabel("Titles Added")

plt.grid(True)

plt.savefig("images/content_added_trend.png")

plt.show()