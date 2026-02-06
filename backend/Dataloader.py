import pandas as pd

def load_data():
    # Placeholder for public cyber datasets
    data = {
        "feature1": [1, 2, 3, 4],
        "feature2": [5, 6, 7, 8],
        "label": ["Normal", "Brute Force", "Ransomware", "DDoS"]
    }
    return pd.DataFrame(data)
