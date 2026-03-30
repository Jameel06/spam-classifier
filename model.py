import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_message(msg):
    msg_tfidf = vectorizer.transform([msg])
    prediction = model.predict(msg_tfidf)[0]
    probability = model.predict_proba(msg_tfidf)[0]

    confidence = max(probability)

    # 🔥 Improved logic
    if confidence < 0.75:
        result = "⚠️ Uncertain"
    elif prediction == 1:
        result = "🚨 Spam"
    else:
        result = "✅ Not Spam"

    return result, confidence