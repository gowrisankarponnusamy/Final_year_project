import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(csv_path):
    df = pd.read_csv(csv_path)
    # Drop non-predictive ID column
    if "session_id" in df.columns:
        df = df.drop("session_id", axis=1)
    # Target variable
    y = df["attack_detected"]

    # Drop target from features
    X = df.drop("attack_detected", axis=1)

    # Encode categorical columns
    categorical_cols = X.select_dtypes(include=["object"]).columns



    encoders = {}

    for col in categorical_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])
        encoders[col] = le

    return X, y, encoders
