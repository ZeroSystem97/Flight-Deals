**About Flight Deals:**\
Flight Deals is a program to check the lowest flight price using Amadeus API and compare them to Google Sheets where is set a City name and users lowest price. If a flight price to desired destination is lower the price set in Google Sheet a text message will be send to the user via Twilio.\
To use this program you need to create a Google Sheet document named **Flight Deals**, and a sheet must be named **prices**, this sheet will contain **City**(A:1), **IATA Code**(B:1), **Lowest Price**(C:1).\
Under the cell named **City**, fill the rows with city names of your desired destination.\
No need to fill the rows under the cell named **IATA Code**, program will fill IATA codes for you from Amadeus database.\
Under the cell named **Lowest Price**, fill the rows with a lowest price you have seen for this destination.\
In project root create a file named **.env** and set these environmental variables:
- SHEETY_USERNAME="Your Sheety username"
- SHEETY_PASSWORD="Your Sheety password"
- SHEETY_PRICES_ENDPOINT="Endpoint to your Sheety project (created from Google Sheet)"
- AMADEUS_API_KEY="Your Amadeus API key"
- AMADEUS_API_SECRET="Your Amadeus API Secret"
- TWILIO_SID="Your Twilio SID"
- TWILIO_AUTH_TOKEN="Your Twilio Authentication Token"
- TWILIO_PHONE_NUMBER="Your Twilio virtual number"
- MY_PHONE_NUMBER="Your phone number or phone number of the receiver (number must be verified in Twilio.)"