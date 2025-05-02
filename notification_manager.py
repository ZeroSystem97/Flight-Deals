import os, smtplib
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.client = Client(username=os.environ["TWILIO_SID"], password=os.environ["TWILIO_AUTH_TOKEN"])
        self.email = os.environ["SMTP_EMAIL"]
        self.password = os.environ["SMTP_PASSWORD"]

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_PHONE_NUMBER"],
            body=message_body,
            to=os.environ["MY_PHONE_NUMBER"]
        )
        print(message.sid)

    def send_emails(self, message_body, customer_emails):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            for email in customer_emails:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:Low price alert!\n\n{message_body}"
                )