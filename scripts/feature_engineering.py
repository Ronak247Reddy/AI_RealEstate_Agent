
import pandas as pd
from sklearn.preprocessing import StandardScaler
from utils.logger import log

def engineer_features(data):
    log("Engineering features...")
    data['price_per_sqft'] = data['price'] / data['sqft']
    data['age'] = 2025 - data['year_built']
    data['luxury_index'] = (data['price'] > 1_000_000) * 1

    # Scale numerical features
    scaler = StandardScaler()
    numerical_features = ['sqft', 'bedrooms', 'bathrooms', 'age']
    data[numerical_features] = scaler.fit_transform(data[numerical_features])
    
    # Encode categorical features
    data = pd.get_dummies(data, columns=['property_type', 'location'], drop_first=True)
    return data

if __name__ == "__main__":
    df = pd.read_csv("data/processed_data/real_estate_data.csv")
    df = engineer_features(df)
    df.to_csv("data/processed_data/engineered_data.csv", index=False)
    