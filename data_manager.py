import requests
from dotenv import load_dotenv
import os
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.sheety_api = "https://api.sheety.co/8210c8b43ce5c9fc1f19c5c5dbb387b8/flightscan/prices"
        self.headers = {
            "Authorization": os.getenv("SHEETY_TOKEN"),
        }
    def sheet_data(self):
        response = requests.get(self.sheety_api, headers = self.headers)
        return(response.json())

    def update_lowest_price(self, destination_id, new_price):
        update_endpoint = f"{self.sheety_api}/{destination_id}"
        body = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(update_endpoint, json=body, headers=self.headers)
        print(response.text)