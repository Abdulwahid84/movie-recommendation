# 🎬 Movie Recommendation System

<img width="1910" height="934" alt="movei recommendation" src="https://github.com/user-attachments/assets/4118bffa-2ab9-4f7f-b676-e44e9fe04e4e" />


A content-based movie recommender system built using Python, Streamlit, and TMDB API.  
This application suggests similar movies based on selected movie metadata such as genre, cast, keywords, and director.

---

## 🚀 Demo

**📍 Localhost Preview (Developer Mode):**  
If you're running locally:  
👉 [http://localhost:8501](http://localhost:8501)

**🌐 Live Demo (Coming soon)**  

---

## 🧠 How it works

This system uses:

- **Text processing + vectorization** of movie metadata (overview, genres, cast, etc.)
- **Cosine similarity** between movies to find the most similar ones
- **TMDB API** to fetch movie posters dynamically

---

## 🖥️ Features

✅ Search any movie from the dataset  
✅ Get top 5 similar movie recommendations  
✅ View posters fetched live via TMDB API  
✅ Clean and responsive Streamlit UI

---



## 🛠️ Tech Stack

| Tool / Library     | Purpose                     |
|--------------------|-----------------------------|
| `pandas`           | Data processing             |
| `scikit-learn`     | Vectorization & similarity  |
| `nltk`             | Text stemming               |
| `ast`              | Safe JSON parsing           |
| `pickle`           | Model serialization         |
| `Streamlit`        | Web app UI                  |
| `requests`         | API calls (TMDB)            |

---
