import pandas as pd
import difflib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -------------------------------------------------
# Load Dataset
# -------------------------------------------------

df = pd.read_csv("dataset/cleaned_netflix.csv")


# -------------------------------------------------
# Feature Engineering
# -------------------------------------------------

features = [
    "listed_in",
    "description",
    "director",
    "cast",
    "country",
    "type",
    "rating"
]

df["combined_features"] = ""

for feature in features:
    df["combined_features"] += df[feature].fillna("") + " "


# -------------------------------------------------
# Build TF-IDF Model
# -------------------------------------------------

vectorizer = TfidfVectorizer(stop_words="english")

tfidf_matrix = vectorizer.fit_transform(df["combined_features"])

similarity_matrix = cosine_similarity(tfidf_matrix)


# -------------------------------------------------
# Fuzzy Search
# -------------------------------------------------

def search_titles(title):

    titles = df["title"].tolist()

    return difflib.get_close_matches(
        title,
        titles,
        n=5,
        cutoff=0.4
    )


# -------------------------------------------------
# Recommendation Function
# -------------------------------------------------

def recommend(title, top_n=5):

    matches = df[df["title"].str.lower() == title.lower()]

    if matches.empty:
        return None

    idx = matches.index[0]

    similarity_scores = list(enumerate(similarity_matrix[idx]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[1:]

    recommendations = []

    original_type = df.iloc[idx]["type"]

    for movie_index, score in similarity_scores:

        if df.iloc[movie_index]["type"] != original_type:
            continue

        recommendations.append({

            "Title": df.iloc[movie_index]["title"],

            "Similarity": f"{score*100:.1f}%",

            "Type": df.iloc[movie_index]["type"],

            "Genre": df.iloc[movie_index]["listed_in"],

            "Rating": df.iloc[movie_index]["rating"],

            "Release Year": df.iloc[movie_index]["release_year"],

            "Description": df.iloc[movie_index]["description"]

        })

        if len(recommendations) == top_n:
            break

    return pd.DataFrame(recommendations)