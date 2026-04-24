import requests_cache
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(180)

#######################  GET SHEET DATA ########################
sheet_data = DataManager()
destinations = sheet_data.sheet_data()


################## SEARCH FLIGHTS ###########################
flight_search = FlightSearch()
notification_manager = NotificationManager()
for destination in destinations["prices"]:
    print(f"Checking flights to {destination["city"]}...")
    flights = flight_search.check_flights("ARN", destination["iataCode"], tomorrow, six_months_from_today)

    if not flights.get("best_flights"):
        print(f"No flights found for {destination['city']}")
        continue
    cheapest_flight = flights["best_flights"][0]
    for flight in flights["best_flights"]:
        if flight["price"] < cheapest_flight["price"]:
            cheapest_flight = flight

    price = cheapest_flight["price"]
    departure = cheapest_flight["flights"][0]["departure_airport"]["id"]
    arrival = cheapest_flight["flights"][-1]["arrival_airport"]["id"]
    outbound_date = cheapest_flight["flights"][0]["departure_airport"]["time"]
    print(f"Roundtrip from {departure} to {arrival} for {price}kr, {outbound_date}")

    if price < destination["lowestPrice"]:
        notification_manager.send_message(
            f"Low price alert! ✈️\n"
            f"Only {price} SEK to fly to {destination['city']}!\n"
            f"From: {departure} → To: {arrival}\n"
            f"Outbound: {outbound_date}\n"
            f"Book now!"
        )
        sheet_data.update_lowest_price(destination["id"], price)