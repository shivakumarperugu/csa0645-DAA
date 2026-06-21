from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Training documents
documents = [
    "football match and cricket tournament",
    "new AI and machine learning technology",
    "stock market and business news",
    "deep learning and data science"
]

categories = [
    "Sports",
    "Technology",
    "Business",
    "Technology"
]

# Create Classification Model
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

# Train Model
model.fit(documents, categories)

# Test Documents
test_docs = [
    "artificial intelligence applications",
    "cricket world cup"
]

predictions = model.predict(test_docs)

for doc, category in zip(test_docs, predictions):
    print(f"Document: {doc}")
    print(f"Category: {category}\n")