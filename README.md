# 📰 Fake News Detection Web App

A full-stack web application that detects whether a given news article is real or fake using machine learning. The frontend is built with React.js and the backend uses Flask (Python) with a trained logistic regression model.

---

## 🚀 Features

- Classifies news articles as Real or Fake
- Clean and responsive UI using modern CSS
- Machine learning model trained on real-world datasets (Fake.csv, True.csv)
- Full integration between React frontend and Flask backend

---

## 🛠️ Tech Stack

| Layer      | Technologies                       |
|------------|------------------------------------|
| Frontend   | React.js, Axios, HTML5, CSS3       |
| Backend    | Python, Flask, Flask-CORS          |
| ML Model   | Scikit-learn, pandas, TF-IDF, Logistic Regression |
| Tools      | Git, VS Code, Postman              |

---

## 📂 Folder Structure

fake-news-detector/
├── ml-backend/ ← Python backend + ML
│ ├── Fake.csv
│ ├── True.csv
│ ├── train_model.py
│ ├── server.py
│ ├── fake_news_model.pkl
│ └── vectorizer.pkl
└── client/ ← React frontend
└── src/
├── components/
│ ├── NewsForm.js
│ └── NewsForm.css
└── App.js


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/pp923014/Fake-News.git
cd fake-news-detector
cd ml-backend
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux

pip install -r requirements.txt
python train_model.py   # Trains and saves the ML model
python server.py        # Starts the Flask server on port 5000
