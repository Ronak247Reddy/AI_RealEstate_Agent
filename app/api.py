
from flask import Flask, request, jsonify
import joblib
import pandas as pd
from utils.logger import log

app = Flask(__name__)
model = joblib.load("models/base_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.json
        input_df = pd.DataFrame(input_data)
        predictions = model.predict(input_df)
        return jsonify({"predictions": predictions.tolist()})
    except Exception as e:
        log(f"Error in prediction: {str(e)}")
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
    