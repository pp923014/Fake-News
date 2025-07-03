from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = joblib.load('fake_news_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    news = data.get("news", "")
    if not news:
        return jsonify({"error": "No news text provided"}), 400

    vect_news = vectorizer.transform([news])
    prediction = model.predict(vect_news)[0]
    result = "Fake" if prediction == 1 else "Real"
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(port=5000)
