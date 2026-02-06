import joblib
import pandas as pd
import random
from .Defender import trigger_defense

MODEL_PATH = "model/attack_model.pkl"

# Load trained model and encoders
model, encoders = joblib.load(MODEL_PATH)

def generate_live_sample():
    """
    Simulate live network data (same structure as dataset)
    """
    sample = {
        "network_packet_size": random.randint(100, 1500),
        "protocol_type": random.choice(["TCP", "UDP"]),
        "login_attempts": random.randint(0, 10),
        "session_duration": random.randint(1, 300),
        "encryption_used": random.choice(["AES", "DES", "None"]),
        "ip_reputation_score": random.randint(1, 100),
        "failed_logins": random.randint(0, 5),
        "browser_type": random.choice(["Chrome", "Firefox", "Edge"]),
        "unusual_time_access": random.choice([0, 1])
    }

    return pd.DataFrame([sample])


def encode_live_data(df):
    """
    Apply same encoders used during training
    """
    for col, encoder in encoders.items():
        if col in df.columns:
            # Handle unseen labels safely
            df[col] = df[col].apply(
                lambda x: encoder.transform([x])[0]
                if x in encoder.classes_ else 0
            )
    return df


def run_prediction():
    df = generate_live_sample()
    df = encode_live_data(df)

    prediction = model.predict(df)[0]
    probability = max(model.predict_proba(df)[0])

    if prediction == 1:
        print(f"[ML] INTRUSION DETECTED | Risk: {probability:.2f}")
        if probability > 0.70:
            trigger_defense("Intrusion", round(probability, 2))
    else:
        print(f"[ML] Normal Traffic | Confidence: {1 - probability:.2f}")
