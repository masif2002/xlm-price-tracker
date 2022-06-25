import requests
import httplib2
import os
from time import sleep
from bs4 import BeautifulSoup
from lxml import etree
from datetime import datetime

def get_price():
    URL = "https://coinmarketcap.com/currencies/stellar/"
    http = httplib2.Http()
    status, response = http.request(URL)

    soup = BeautifulSoup(response, "html.parser")
    dom = etree.HTML(str(soup))
    xp = '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[4]/span[2]/div/div'
    return dom.xpath(f'{xp}')[0].text


def send_message(time, price, alert):
    # Getting all the environment variables for the application from Heroku
    API_TOKEN = os.environ.get('API_TOKEN')
    CHAT_ID1 = os.environ.get('CHAT_ID1')   # ChatID for Price Alerts  
    CHAT_ID2 = os.environ.get('CHAT_ID2')   # ChatID for Daily Prices
    TEXT = f"XLM price: {price} %0Afetched at {time} UTC"
    
    # Sends XLM rates regularly
    URL = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage?text={TEXT}&chat_id={CHAT_ID2}"
    requests.get(URL)

    if (alert):
        # Sends Only Alerts
        URL = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage?text={TEXT}&chat_id={CHAT_ID1}"
        requests.get(URL)

while True:
    current_time = datetime.now()
    current_price = get_price()
    PRICE = float(os.environ.get('PRICE'))
    alert = False

    if (float(current_price[1:]) >= PRICE):
        alert = True
    send_message(time=str(current_time)[:16], price=current_price, alert=alert)
    sleep(3600)