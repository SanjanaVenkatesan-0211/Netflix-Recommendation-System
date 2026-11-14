# Netflix Recommendation System

A content-based movie and TV show recommender built with Python, pandas, scikit-learn, and Streamlit. The app suggests titles similar to a user-selected Netflix title by analyzing metadata such as genre, description, director, cast, country, type, and rating.

## Features

- Search for a movie or TV show by title
- Fuzzy matching for close title suggestions
- Content-based recommendations using TF-IDF and cosine similarity
- Filters recommendations to the same media type (movie vs TV show)
- Clean, interactive UI created with Streamlit

## Tech Stack

- Python 3
- Streamlit
- pandas
- scikit-learn
- SQLite (used in the project database scripts)

## Project Structure

```text
Netflix-Recommendation-System/
├── app.py                     # Streamlit application entry point
├── dataset/
│   ├── cleaned_netflix.csv    # Cleaned dataset used by the recommender
│   └── netflix_titles.csv     # Raw Netflix dataset
├── src/
│   ├── data_cleaning.py       # Data cleaning and preprocessing
│   ├── load_data.py           # Quick dataset inspection utilities
│   ├── recommendation.py      # TF-IDF recommender logic
│   ├── eda.py                 # Exploratory data analysis scripts
│   ├── sql_analysis.py        # SQL-based data analysis
│   ├── visualization.py       # Visualizations
│   └── create_database.py     # Database setup logic
├── notebooks/                 # Jupyter notebooks and experiments
├── sql/
│   └── queries.sql            # SQL sample queries
├── images/                    # Project screenshots and assets
├── requirements.txt           # Python dependency list
├── netflix.db                 # Local SQLite database file
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore rules
```

## How the Recommendation Engine Works

The recommender combines several text fields from each title into a single text string:

- genre
- description
- director
- cast
- country
- type
- rating

It then converts this text into numerical vectors using TF-IDF and computes similarities with cosine similarity. For a selected title, the system ranks other titles by similarity and presents the top matches.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Netflix-Recommendation-System.git
cd Netflix-Recommendation-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

On Windows:

```powershell
venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

The app should open in your browser, where you can type a title and click the Recommend button.

## Data Preparation

The data cleaning script prepares the raw Netflix dataset before generating recommendations:

```bash
python src/data_cleaning.py
```

This script:

- removes duplicate records
- fills missing values
- converts date fields
- saves the cleaned dataset to `dataset/cleaned_netflix.csv`

## Example Usage

1. Launch the app with Streamlit.
2. Enter a title such as "Stranger Things" or "The Crown".
3. Click Recommend.
4. Review the top similar titles, similarity score, genre, and description.

## Notes

- The recommender is based on metadata similarity rather than user behavior or collaborative filtering.
- The fuzzy search feature helps when the input title is slightly misspelled or incomplete.
- Recommendations are intentionally limited to the same media type for more relevant results.

## License

This project is for educational and personal use. If you are sharing or publishing it, please mention the source dataset and project attribution where applicable.

## Future Improvements

- Add user-based collaborative filtering
- Include poster images for each recommendation
- Add a richer dashboard with charts and popularity analysis
- Add better search and ranking customization
- Deploy the app using Streamlit Cloud or Heroku
