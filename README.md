A Python automation tool that monitors flight prices and sends SMS alerts when cheap deals are found. Built as part of the 100 Days of Python course.
What It Does

Reads a list of destinations and target prices from a Google Sheet
Searches for the cheapest available flights from Stockholm Arlanda (ARN) using the Google Flights API
Sends an SMS notification when a flight is found below your target price
Automatically updates the Google Sheet with the new lowest price found

Project Structure
FlightScanner/
├── main.py                  # Entry point, orchestrates the flow
├── data_manager.py          # Handles Google Sheets via Sheety
├── flight_search.py         # Handles flight search via SerpAPI
├── notification_manager.py  # Handles SMS notifications via Twilio
├── .gitignore
└── README.md
Setup
1. Install dependencies
bashpip install requests requests-cache python-dotenv twilio
2. Set up your Google Sheet
Create a Google Sheet with these columns and connect it to Sheety:
CityIATA CodeLowest PriceParisCDG540FrankfurtFRA12345TokyoHND4850
3. Create a .env file with your API keys
SERPAPI_API_KEY=your_serpapi_key
SHEETY_TOKEN=your_sheety_token
TWILIO_SID=your_twilio_account_sid
TWILIO_TOKEN=your_twilio_auth_token
TWILIO_FROM_NUMBER=your_twilio_phone_number
TWILIO_TO_NUMBER=your_personal_phone_number
4. Run
bashpython main.py
Example SMS Alert
Low price alert! ✈️
Only 2560 SEK to fly to Frankfurt!
From: ARN → To: FRA
Outbound: 2026-04-25 09:50
Book now!
