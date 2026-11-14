import streamlit as st

from src.recommendation import recommend, search_titles


# ---------------------------
# Page Configuration
# ---------------------------

st.set_page_config(
    page_title="Netflix Recommendation System",
    page_icon="🎬",
    layout="wide"
)


# ---------------------------
# Title
# ---------------------------

st.title("🎬 Netflix Recommendation System")

st.write(
    "Find movies and TV shows similar to your favorite Netflix title."
)

st.divider()


# ---------------------------
# Search Box
# ---------------------------

movie_name = st.text_input(
    "Enter Movie / TV Show Name"
)


# ---------------------------
# Recommend Button
# ---------------------------

if st.button("Recommend"):

    if movie_name.strip() == "":
        st.warning("Please enter a movie name.")

    else:

        recommendations = recommend(movie_name)

        if recommendations is not None:

            st.success(
                f"Top {len(recommendations)} Recommendations"
            )

            st.dataframe(
                recommendations,
                use_container_width=True
            )

        else:

            st.error("Movie not found.")

            suggestions = search_titles(movie_name)

            if suggestions:

                st.write("Did you mean:")

                for movie in suggestions:

                    st.write(f"• {movie}")