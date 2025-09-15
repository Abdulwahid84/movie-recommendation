# 🎬 Movie Recommendation System

A content-based movie recommender system built using Python, Streamlit, and TMDB API.  
This application suggests similar movies based on selected movie metadata such as genre, cast, keywords, and director.

---

## 🚀 Demo

**📍 Localhost Preview (Developer Mode):**  
If you're running locally:  
👉 [http://localhost:8501](http://localhost:8501)

**🌐 Live Demo (Coming soon)**  
> You can deploy this app on [Streamlit Cloud](https://streamlit.io/cloud) to get a live shareable link.

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

## 🧪 Sample Screenshot

Here’s a preview of the app running on localhost:

![Home Screen](screenshot.png)

> _This is the main screen showing the movie selector and "Show Recommendation" button._

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

## 🧰 Getting Started

Follow the steps below to run this project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/Abdulwahid84/movie-recommendation.git
cd movie-recommendation
