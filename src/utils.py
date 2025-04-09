import requests
import pandas as pd
from src.exception_handler import handle_exception
from src.logger import logging

def fetch_firebase_json_as_dataframe(firebase_url: str) -> pd.DataFrame:
    """
    Fetch JSON data from Firebase Realtime Database and convert it into a pandas DataFrame.
    """
    try:
        url = firebase_url.rstrip('/') + '.json'
        logging.info(f"Fetching data from Firebase: {url}")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if not data:
            raise ValueError("Received empty data from Firebase.")

        if isinstance(data, list):
            df = pd.DataFrame(data)
        elif isinstance(data, dict):
            df = pd.DataFrame.from_dict(data, orient='index')
        else:
            raise ValueError("Unexpected data format from Firebase.")

        return df

    except Exception as e:
        raise handle_exception(e)
