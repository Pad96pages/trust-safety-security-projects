import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump

df = pd.read_csv("data/threat_small.csv")

X_train, X_test, y_train, y_test = train_test_split(
    df.text, df.label, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
vectorizer = TfidfVectorizer()

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model.fit(X_train_vec, y_train)

print("Train Accuracy:", model.score(X_train_vec, y_train))
print("Test Accuracy:", model.score(X_test_vec, y_test))

dump(vectorizer, "models/vectorizer.joblib")
dump(model, "models/threat_model.joblib")

print("Saved model + vectorizer inside models/")
