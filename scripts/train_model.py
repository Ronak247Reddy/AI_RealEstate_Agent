
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd
import joblib
from utils.logger import log

def train_model(data_path):
    log("Starting model training...")
    data = pd.read_csv(data_path)
    X = data.drop(columns=['price'])
    y = data['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = XGBRegressor(n_estimators=500, learning_rate=0.05, max_depth=6, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    log(f"MAE: {mean_absolute_error(y_test, predictions):.2f}")
    log(f"RMSE: {mean_squared_error(y_test, predictions, squared=False):.2f}")

    joblib.dump(model, "models/base_model.pkl")
    log("Model training completed and saved.")

if __name__ == "__main__":
    train_model("data/processed_data/engineered_data.csv")
    