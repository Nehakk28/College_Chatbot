import json
import pickle
import nltk
import re
import os

from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load intents
with open('dataset/intents1.json') as file:
    data = json.load(file)

sentences = []
labels = []

# Preprocessing function
def preprocess(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words if word.isalpha()]
    return " ".join(words)

# Prepare training data
for intent in data['intents']:
    for pattern in intent['patterns']:
        sentences.append(preprocess(pattern))
        labels.append(intent['tag'])

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(sentences)

# Model
model = LogisticRegression()
model.fit(X, labels)

os.makedirs("model", exist_ok=True)

# Save model
pickle.dump(model, open('model/chatbot_model.pkl', 'wb'))
pickle.dump(vectorizer, open('model/vectorizer.pkl', 'wb'))

print("✅ Model trained successfully!")