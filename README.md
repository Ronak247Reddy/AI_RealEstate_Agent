
# AI Real Estate Agent

## Overview
This project implements a machine learning-based real estate agent capable of predicting property values with high accuracy. 
It dynamically updates based on real-time data and includes advanced feature engineering and modeling techniques.

## Features
- Predict real estate prices with minimal error using XGBoost and ensemble models.
- Dynamically adapt to market trends with real-time updates and retraining.
- Scalable Flask API for predictions.
- Modular scripts for data collection, preprocessing, feature engineering, and training.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/AI_RealEstate_Agent.git
   ```

2. Navigate to the project directory:
   ```bash
   cd AI_RealEstate_Agent
   ```

3. Install dependencies:
   ```bash
   pip install -r app/requirements.txt
   ```

## Usage
### Data Collection
Run the following to collect real estate data:
```bash
python app/data_collector.py
```

### Preprocessing and Feature Engineering
```bash
python scripts/data_preprocessing.py
python scripts/feature_engineering.py
```

### Model Training
```bash
python scripts/train_model.py
```

### Start the API
```bash
python app/api.py
```

### Make Predictions
Use a tool like `curl` or Postman to make predictions via the API.
Example:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"sqft": [2000], "location": ["New York"], "bedrooms": [3], "bathrooms": [2]}' http://127.0.0.1:5000/predict
```

## Future Enhancements
- Integrate additional real estate APIs.
- Build a dashboard for visualizing trends.
- Incorporate deep learning models.

## License
MIT License.
    