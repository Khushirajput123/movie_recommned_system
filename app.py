import pickle
import pandas as pd
import streamlit as st
import requests

# --- Fetch movie poster ---
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=406c9859c5a1513e1a844c6486338327&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')
    return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ""

# --- Recommend movies ---
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# --- Load data ---
movies_dict = pickle.load(open('movie.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
movie_titles = movies['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

# --- Page Config ---
st.set_page_config(page_title="Movie Recommender", layout="wide")

# --- Global Styling ---
st.markdown(
    """
    <style>
    /* App background and text colors */
    .stApp {
        background-color: #121212;
        color: #ffffff;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }

    /* Title styling */
    h1 {
        text-align: center;
        font-size: 42px !important;
        font-weight: 700 !important;
        background: linear-gradient(90deg, #ff8c00, #ff3c3c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }

    /* Subheading */
    h3 {
        color: #ffb347 !important;
        font-weight: 600 !important;
    }

    /* Custom button styling */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #ff8c00, #ff3c3c);
        color: white;
        border: none;
        padding: 0.6em 1.5em;
        border-radius: 25px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease-in-out;
        display: block;
        margin: auto;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #ff3c3c, #ff8c00);
        transform: scale(1.05);
        box-shadow: 0px 4px 12px rgba(255, 140, 0, 0.5);
    }

    /* Poster styling */
    [data-testid="stImage"] img {
        height: 300px;
        object-fit: cover;
        border-radius: 12px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.7);
    }

    /* Movie name styling */
    .movie-title {
        text-align: center;
        font-weight: bold;
        font-size: 16px;
        color: #ffb347;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.title('🍿 Movie Recommendation System')

# --- Movie selection ---
selected_movie_name = st.selectbox('🎬 **Choose a movie you like:**', movie_titles)

# --- Button and Recommendations ---
if st.button('🔎 Recommend Movies'):
    names, posters = recommend(selected_movie_name)

    st.markdown("### 🎥 **Top 10 Recommendations for You:**")
    st.write("---")

    # Display in rows of 5
    for row in range(0, len(names), 5):
        cols = st.columns(5, gap="large")
        for idx, col in enumerate(cols):
            if row + idx < len(names):
                with col:
                    st.markdown(
                        f"<div class='movie-title'>{names[row + idx]}</div>",
                        unsafe_allow_html=True
                    )
                    st.image(posters[row + idx], use_container_width=True, caption="")






