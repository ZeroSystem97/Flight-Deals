import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.client = Client(username=os.environ["TWILIO_SID"], password=os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_PHONE_NUMBER"],
            body=message_body,
            to=os.environ["MY_PHONE_NUMBER"]
        )
        print(message.sid)