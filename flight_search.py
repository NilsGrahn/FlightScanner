import requests
import requests_cache
from dotenv import load_dotenv
import os
class FlightSearch:
    def __init__(self):
        load_dotenv()
        self.SERPAPI_ENDPOINT = "https://serpapi.com/search?engine=google_flights"
        self._api_key = os.environ["SERPAPI_API_KEY"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        params = \
            {
              "engine": "google_flights",
              "departure_id": origin_city_code,
              "arrival_id": destination_city_code,
              "outbound_date": from_time.strftime("%Y-%m-%d"),
              "return_date": to_time.strftime("%Y-%m-%d"),
              "type": "1",
              "adults": "1",
              "currency": "SEK",
              "api_key": self._api_key,
            }
        response = requests.get(self.SERPAPI_ENDPOINT, params=params)
        return response.json()