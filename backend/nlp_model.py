import pickle
import re
import os

# locate backend folder automatically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# load trained files
model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
vec = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))


def clean_text(text):
    text = str(text).lower()
    return re.sub(r'[^a-zA-Z ]', '', text)


def predict_violation(text):

    cleaned_text = clean_text(text)

    X = vec.transform([cleaned_text])

    prediction = model.predict(X)[0]

    return {
        "violation": str(prediction),
        "score": 0.9 if str(prediction) == "violation" else 0.2
    }