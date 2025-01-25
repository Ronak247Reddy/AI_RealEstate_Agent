
import requests
import pandas as pd
from utils.logger import log

API_KEY = "your_api_key"
BASE_URL = "https://realestateapi.com/data"

def fetch_real_estate_data(location, max_results=100):
    log("Fetching real estate data...")
    params = {
        "location": location,
        "limit": max_results,
        "api_key": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['listings'])
        df.to_csv(f"data/raw_data/real_estate_{location}.csv", index=False)
        log(f"Fetched {len(df)} records for {location}.")
        return df
    else:
        log(f"Failed to fetch data: {response.status_code}")
        return None

if __name__ == "__main__":
    fetch_real_estate_data("New York")
    