
# 🎬 Movie Recommendation System

<img width="1910" height="934" alt="movie recommendation" src="https://github.com/user-attachments/assets/4118bffa-2ab9-4f7f-b676-e44e9fe04e4e" />

A **content-based movie recommender system** built using Python, Streamlit, and the TMDB API.  
This application suggests movies similar to your selected choice based on metadata such as genre, cast, keywords, and director.

---

## 🚀 Demo

**📍 Localhost Preview (Developer Mode):**  
If you're running locally:  
👉 [http://localhost:8501](http://localhost:8501)

**🌐 Live Demo (Coming soon)**

---

## 🧠 How It Works

This system uses:

- **Text processing + vectorization** of movie metadata (overview, genres, cast, etc.)  
- **Cosine similarity** to find the most similar movies  
- **TMDB API** to fetch movie posters dynamically  

---

## 🖥️ Features

- ✅ Search any movie from the dataset  
- ✅ Get top 5 similar movie recommendations  
- ✅ View posters fetched live via TMDB API  
- ✅ Clean and responsive Streamlit UI  

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

## ⚡ Installation

1. **Clone the repository**

git clone https://github.com/Abdulwahid84/movie-recommendation.git
cd movie-recommendation


2. **Install dependencies**


pip install -r requirements.txt


3. **Run the app**


streamlit run app.py




## 🚀 Usage

1. Open the app in your browser.
2. Search for a movie by typing its name.
3. See the **top 5 recommended movies** with their posters.
4. Explore similar movies and enjoy!


## 📦 Dependencies

* Python 3.x
* pandas
* scikit-learn
* nltk
* ast
* pickle
* Streamlit
* requests

---

## 👥 Contributors

* **Abdulwahid84** – [GitHub Profile](https://github.com/Abdulwahid84)

