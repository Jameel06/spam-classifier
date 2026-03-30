import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_message(msg):
    msg_tfidf = vectorizer.transform([msg])
    prediction = model.predict(msg_tfidf)[0]
    probability = model.predict_proba(msg_tfidf)[0]

    confidence = max(probability)

    # 🔥 Improved logic
    if prediction == 1 and confidence > 0.55:
         result = "🚨 Spam"
    elif prediction == 0 and confidence > 0.55:
         result = "✅ Not Spam"
    else:
         result = "⚠️ Uncertain"

    return result, confidence
