import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load data
fake_df = pd.read_csv("Fake.csv")
true_df = pd.read_csv("True.csv")

# Add labels: 1 = Fake, 0 = Real
fake_df["label"] = 1
true_df["label"] = 0

# Combine datasets
df = pd.concat([fake_df, true_df], axis=0)

# Shuffle data
df = df.sample(frac=1).reset_index(drop=True)

# Create content column
df['content'] = df['title'].astype(str) + " " + df['text'].astype(str)

# Drop rows with missing content
df = df.dropna(subset=['content', 'label'])

# Features and target
X = df['content']
y = df['label']

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_vec = vectorizer.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate
pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)
print(f"Accuracy: {acc:.2f}")

# Save model and vectorizer
joblib.dump(model, 'fake_news_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
