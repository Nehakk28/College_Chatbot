# from flask import Flask, render_template, request
# import pickle
# import json
# import random
# import re
# import nltk
# from nltk.stem import WordNetLemmatizer

# nltk.download('punkt')
# nltk.download('wordnet')

# app = Flask(__name__)
# lemmatizer = WordNetLemmatizer()

# def preprocess(text):
#     text = text.lower()
#     words = nltk.word_tokenize(text)
#     words = [lemmatizer.lemmatize(word) for word in words if word.isalpha()]
#     return " ".join(words)

# # Load the trained model and vectorizer
# with open('model/chatbot_model.pkl', 'rb') as f:
#     best_model = pickle.load(f)

# with open('model/vectorizer.pkl', 'rb') as f:
#     vectorizer = pickle.load(f)

# # Load the intents data
# with open('dataset/intents1.json', 'r') as f:
#     intents = json.load(f)

# def chatbot_response(user_input):
#     # input_text = vectorizer.transform([user_input])
#     # predicted_intent = best_model.predict(input_text)[0]

#     # for intent in intents['intents']:
#     #     if intent['tag'] == predicted_intent:
#     #         response = random.choice(intent['responses'])
#     #         break

#     # return response
#     print("Original:", user_input)

#     user_input = preprocess(user_input)
#     print("Processed:", user_input)

#     input_text = vectorizer.transform([user_input])
    
#     predicted_intent = best_model.predict(input_text)[0]
#     probability = max(best_model.predict_proba(input_text)[0])

#     print("Intent:", predicted_intent)
#     print("Confidence:", probability)
    
#     if probability < 0.02:
#         return "Sorry, I didn't understand that."

#     for intent in intents['intents']:
#         if intent['tag'] == predicted_intent:
#             return random.choice(intent['responses'])

#     return "Sorry, something went wrong."

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.form['user_input']
#     response = chatbot_response(user_input)
#     return response

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import json
import random
from thefuzz import process

app = Flask(__name__)

# --- 1. Load the Dataset ---
with open('dataset/intents1.json') as file:
    data = json.load(file)

# --- 2. Your Logic Function ---
def get_response(user_input):
    all_patterns = []
    pattern_to_tag = {}
    
    # Flattening the JSON for fuzzy matching
    for intent in data['intents']:
        for pattern in intent['patterns']:
            all_patterns.append(pattern)
            pattern_to_tag[pattern] = intent['tag']

    # Use Fuzzy Matching (Handles typos like "admition")
    match, score = process.extractOne(user_input, all_patterns)

    if score > 85: 
        tag = pattern_to_tag[match]
        for intent in data['intents']:
            if intent['tag'] == tag:
                return random.choice(intent['responses'])
    
    return "I'm sorry, I don't have information on that yet. Please contact the Holy Grace office at Mala."

# --- 3. Routes ---

@app.route('/')
def index():
    # Renders your index.html file
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # This matches the url: '/chat' in your AJAX call
    user_text = request.form.get('user_input')
    
    if not user_text:
        return "Please say something!"
        
    bot_reply = get_response(user_text)
    return bot_reply

if __name__ == '__main__':
    app.run(debug=True)