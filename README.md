# Movie Recommendation System (Content-Based Filtering)
This project builds a **Movie Recommendation System** using the **Content-Based Filtering** approach.
The system recommends movies similar to a selected movie by analyzing movie metadata.
The model compares movie features and finds the **most similar movies based on their content**.
## Dataset
The dataset contains **approximately 5,000 movies** with metadata used to generate recommendations.
### Features Used
* **Genres** – Movie genre categories
* **Cast** – Main actors in the movie
* **Crew** – Director and production team
* **Keywords** – Important tags related to the movie
* **Overview** – Short description of the movie
These features are combined and processed to compute similarity between movies.
## How the Recommendation Works
The system follows these steps:
1. Load the movie dataset using **Pandas**
2. Combine important metadata features (genres, cast, crew, keywords, overview)
3. Convert text data into numerical form using **Scikit-learn vectorization**
4. Compute **cosine similarity** between movies
5. Recommend the **most similar movies** to the selected movie
## Technologies Used
* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit** (for web interface)
## Project Structure
```
├── app.py              # Streamlit frontend application
├── model.py            # Data preprocessing and similarity model generation
├── movies.csv          # Movie dataset (~5000 records)
├── similarity.pkl      # Precomputed similarity matrix
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Ignore large files and environment folders
```
## Important Note
`similarity.pkl` is **not uploaded to GitHub** because the file size is **larger than 100MB**.
You can regenerate the similarity matrix locally by running:

```
python model.py
```
This will recreate the **similarity model used by the recommendation system**.
## Objective
 goal of this project is to demonstrate how **content-based recommendation systems** work using movie metadata and similarity measures.
The system suggests movies that have **similar characteristics to the movie selected by the user**.
