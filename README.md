# 🤖 E-Commerce FAQ Chatbot

An AI-powered FAQ chatbot developed as part of the **CodeAlpha Internship – Task 2**. The chatbot provides quick answers to frequently asked questions related to e-commerce customer support.

## 📌 Project Overview

The E-Commerce FAQ Chatbot uses **Natural Language Processing (NLP)** to understand user questions and find the most relevant answer from a predefined FAQ dataset.

The system preprocesses the FAQ questions, converts the text into numerical vectors using **TF-IDF (Term Frequency–Inverse Document Frequency)**, and compares the user's question with the available FAQs using **Cosine Similarity**.

The most relevant FAQ answer is displayed through a modern web-based chatbot interface.

## ✨ Features

- 💬 Interactive chatbot interface
- 🛒 E-commerce customer support FAQs
- 🧠 NLP-based text preprocessing
- 📊 TF-IDF vectorization
- 🔍 Cosine similarity-based FAQ matching
- 🎯 Similarity threshold for handling unrelated questions
- 📦 50 predefined FAQ question-answer pairs
- 🔄 Supports multiple questions in the same conversation
- ❌ Fallback response for unrelated questions
- 📱 Responsive and modern user interface
- ⚡ Flask-based web application

## 📂 FAQ Categories

The chatbot contains FAQs from the following categories:

1. Orders & Shipping
2. Payments
3. Delivery
4. Returns & Refunds
5. Account
6. Products
7. Warranty & Support

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| NLTK | Natural Language Processing |
| Scikit-learn | TF-IDF and Cosine Similarity |
| HTML | Web page structure |
| CSS | User interface design |
| JavaScript | Chat interaction |
| JSON | FAQ dataset storage |

## 🧠 How It Works

The chatbot follows these steps:

```text
User enters a question
        ↓
Text preprocessing using NLTK
        ↓
TF-IDF vectorization
        ↓
Cosine similarity calculation
        ↓
Compare with FAQ questions
        ↓
Find the most relevant FAQ
        ↓
Check similarity threshold
        ↓
Display the matching answer
```

If the similarity score is below the defined threshold, the chatbot returns a fallback response instead of providing an unrelated answer.

## 📁 Project Structure

```text
CodeAlpha_ChatbotForFAQs/
│
├── app.py
├── faqs.json
├── requirements.txt
├── README.md
├── .gitignore
│
└── templates/
    └── index.html
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/CodeAlpha_ChatbotForFAQs.git
```

### 2. Open the project folder

```bash
cd CodeAlpha_ChatbotForFAQs
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Open the chatbot

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

## 🧪 Example Questions

The chatbot can answer questions such as:

- How can I place an order?
- Where can I track my package?
- What payment methods do you accept?
- My payment failed. What should I do?
- How can I return a product?
- How long does a refund take?
- I forgot my password.
- How do I create an account?
- How can I claim my warranty?

For unrelated questions such as:

```text
What is the weather today?
```

the chatbot provides a fallback response:

```text
Sorry, I couldn't find a relevant answer to your question.
```

## 🎯 Project Objective

The objective of this project is to develop an intelligent FAQ chatbot that can automatically identify the most relevant answer to an e-commerce customer query using Natural Language Processing and text similarity techniques.

## 👩‍💻 Developed For

**CodeAlpha Internship – Task 2**

**Project:** Chatbot for FAQs

**Domain:** E-Commerce Customer Support

## 📜 License

This project is developed for educational and internship purposes.