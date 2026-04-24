from twilio.rest import Client
from dotenv import load_dotenv
import os

class NotificationManager:
    def __init__(self):
        load_dotenv()
        self.client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))

    def send_message(self, message):
        msg = self.client.messages.create(
            from_=os.getenv("TWILIO_FROM_NUMBER"),
            body=message,
            to=os.getenv("TWILIO_TO_NUMBER")
        )
        print(msg.status)
