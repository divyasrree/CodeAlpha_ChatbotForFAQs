import json
import re

import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, render_template, request, jsonify


# Create Flask application
app = Flask(__name__)


# Load FAQ data
with open("faqs.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)


# Preprocess text using NLTK
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    tokens = word_tokenize(text)

    # Remove common English stopwords
    stop_words = set(nltk.corpus.stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)


# Prepare FAQ questions
faq_questions = [faq["question"] for faq in faqs]
processed_questions = [preprocess_text(question) for question in faq_questions]


# Convert FAQ questions into TF-IDF vectors
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)


# Find the best matching FAQ
def get_response(user_question):
    processed_question = preprocess_text(user_question)

    user_vector = vectorizer.transform([processed_question])

    similarities = cosine_similarity(user_vector, faq_vectors)[0]

    best_match_index = similarities.argmax()
    best_score = similarities[best_match_index]

    # Minimum similarity required for a valid answer
    if best_score < 0.25:
        return "Sorry, I couldn't find a relevant answer to your question."

    return faqs[best_match_index]["answer"]


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Receive user's question and return chatbot response
@app.route("/get_response", methods=["POST"])
def chatbot_response():
    data = request.get_json()

    user_question = data.get("question", "")

    if not user_question.strip():
        return jsonify({
            "response": "Please enter a question."
        })

    response = get_response(user_question)

    return jsonify({
        "response": response
    })


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)