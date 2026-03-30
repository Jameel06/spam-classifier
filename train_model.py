import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load dataset
df = pd.read_csv("spam.csv", sep="\t", names=["label", "message"], encoding="latin-1")
df.dropna(inplace=True)

# Convert labels
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# 🔥 Add custom financial scam data
extra_data = pd.DataFrame({
    "label": [1,1,1,1,1],
    "message": [
        "Earn ₹50,000 per week from home",
        "Invest ₹10,000 and get ₹1 lakh instantly",
        "Work from home no experience needed high income",
        "Crypto investment guaranteed returns",
        "Double your money in 7 days"
    ]
})

df = pd.concat([df, extra_data], ignore_index=True)

# Vectorization (IMPROVED)
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))

X = vectorizer.fit_transform(df['message'])
y = df['label']

# Model (BETTER for text)
model = MultinomialNB()
model.fit(X, y)

# Save files
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained and saved!")