Content-Based Filtering Approach
This is a Movie Recommendation System built using Content-Based Filtering.
The system recommends movies similar to the selected movie by using metadata such as:
Genres
Cast
Crew
Keywords
Movie overview
The project is built in Python using Pandas, NumPy, Scikit-learn, and deployed using Streamlit.
Project Structure
├── app.py                 # Streamlit frontend file
├── model.py               # Script to preprocess data and generate similarity matrix
├── movies.csv             # Dataset of movies
├── similarity.pkl         # Precomputed similarity model (ignored in GitHub)
├── requirements.txt       # Dependencies
├── README.md              # Documentation
└── .gitignore             # Ignore large files like .pkl and .venv
⚠ Note:
similarity.pkl is NOT uploaded to GitHub because it is larger than 100MB.
You can regenerate it by running model.py.
