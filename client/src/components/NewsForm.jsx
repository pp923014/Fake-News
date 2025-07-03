import React, { useState } from "react";
import axios from "axios";
import "./NewsForm.css"; // ✅ Import the CSS file

const NewsForm = () => {
  const [news, setNews] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult("");

    try {
      const res = await axios.post("http://localhost:5000/predict", { news });
      setResult(res.data.prediction);
    } catch (err) {
      console.error(err);
      setResult("An error occurred while predicting.");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <div className="form-box">
        <h1 className="title">📰 Fake News Detector</h1>
        <form onSubmit={handleSubmit}>
          <textarea
            className="news-input"
            placeholder="Paste your news article here..."
            value={news}
            onChange={(e) => setNews(e.target.value)}
            required
          ></textarea>
          <button type="submit" className="submit-btn">
            {loading ? "Checking..." : "Check News"}
          </button>
        </form>

        {result && (
          <div className={`result ${result === "Fake" ? "fake" : "real"}`}>
            Result: {result}
          </div>
        )}
      </div>
    </div>
  );
};

export default NewsForm;
