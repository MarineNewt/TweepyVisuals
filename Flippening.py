import numpy as np
import pandas as pd
import requests
from requests import Request, Session
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import tweepy
import keys

##Twitter bot for determining how close Etherum is to Bitcoin's marketcap

url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
parameters = {
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': keys.cmcApiKey,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    # next we create and store the JSON result into a Pandas Dataframe
    data_pd = pd.DataFrame(data)  
   # data_pd = pd.DataFrame(data, index=[1]) 
    
    # Give it a filename 
    OUTPUT_FILENAME = "Latestdata.csv"      
    # and output our results to a CSV!
    data_pd.to_csv(OUTPUT_FILENAME)  
    #Retrieve eth and btc dominance then calculate flippening percent
    ethdom = data_pd.iat[11,1] 
    btcdom = data_pd.iat[12,1] 
    flippening = int((ethdom/btcdom)*100)

    client = tweepy.Client( bearer_token=keys.bearertoken, 
                    consumer_key=keys.consumerkey, 
                    consumer_secret=keys.consumersecret, 
                    access_token=keys.accesstoken, 
                    access_token_secret=keys.accesstokensecret, 
                    wait_on_rate_limit=True)
    stringtext = "The Flippening is " + str(flippening) + "%" + " complete"
    response = client.create_tweet(text= stringtext)
    print(response)

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
