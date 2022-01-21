import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
from bs4 import BeautifulSoup

#env variables
load_dotenv()
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")

#get info
burge = requests.get("https://dining.uiowa.edu/burge-market-place")
soup = BeautifulSoup(burge.text, features="html.parser")
international_burge = soup.find(class_="panel panel-default marketplace-station marketplace-station-Burge-International")
foods = international_burge.find_all(class_="h6 menu-item-title")

#format string
string = "Today's Menu:\n"
for f in foods:
  string += f.text + "\n"

#send text
client = Client(ACCOUNT_SID, AUTH_TOKEN)
with open("./numbers.txt") as numbers:
  for number in numbers:
    client.messages.create(to=number, from_=TWILIO_NUMBER, body=string)