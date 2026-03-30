# College Chatbot using ML & NLP

The College Chatbot is a web-based application built using Python, Machine Learning, and Natural Language Processing (NLP). It is designed to answer student queries related to college information such as courses, admissions, departments, and general FAQs. The chatbot improves user experience by providing quick and automated responses.

## Features
- Interactive chatbot interface
- Intent recognition using Machine Learning
- NLP-based text preprocessing
- Real-time responses using Flask
- Accurate query classification
- Web-based user interface

## Tech Stack
Language: Python
Framework: Flask
ML Library: Scikit-learn
NLP: NLTK
Frontend: HTML, CSS
Dataset: JSON (intents.json)

## Project Structure

College-Chatbot/
│── app.py                 # Main Flask application
│── train.py               # Model training script           
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
│
├── templates/
│   └── index.html         # Frontend UI
│
├── static/
│   └── styles.css         # Styling
│
├── model/                 # Trained model files
│
└── dataset/  
      └── intents.json     # Dataset for chatbot

      
## Installation & Setup

1️. Clone the repository
git clone https://github.com/Nehakk28/College_Chatbot.git
cd College_Chatbot

2️. Create virtual environment
python -m venv venv
venv\Scripts\activate   

3️. Install dependencies
pip install -r requirements.txt

4️. Train the model
python train.py

5️. Run the application
python app.py

Open browser and go to: http://127.0.0.1:5000


