import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from joblib import dump

df = pd.read_csv("data/moderation_small.csv")

X_train, X_test, y_train, y_test = train_test_split(df.text, df.label,
                                                    test_size=0.2, random_state=42)

model = make_pipeline(
    TfidfVectorizer(ngram_range=(1,2)),
    LogisticRegression(max_iter=1000)
)

model.fit(X_train, y_train)

print("Training accuracy:", model.score(X_train, y_train))
print("Test accuracy:", model.score(X_test, y_test))

dump(model, "models/moderation_model.joblib")
print("Model saved in models/moderation_model.joblib")
