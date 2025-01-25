
import pandas as pd
from utils.logger import log

def preprocess_data(file_path):
    log("Preprocessing data...")
    data = pd.read_csv(file_path)
    data.drop_duplicates(inplace=True)
    data.fillna(data.median(), inplace=True)
    return data

if __name__ == "__main__":
    processed_data = preprocess_data("data/raw_data/sample.csv")
    processed_data.to_csv("data/processed_data/processed_data.csv", index=False)
    