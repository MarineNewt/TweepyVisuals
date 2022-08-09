import numpy as np
import tweepy
import keys
import requests

##Twitter bot for sharing quick aesthetic outputs using tweepy library



def seagenerate():
    ##Creates ocean emoji art, using 130 emoji for phone viewing optimization
    stringtext=""
    stringer=""
    unit=""
    passer=0
    for i in range(130):

        #Ocean build
        fish = 0
        x = (np.random.randint(0, 101))
        xx = (np.random.randint(0, 101))
        #boat
        if x <= 100:
            #sailboat
            if xx <= 100:
                unit = '\U000026F5'        
            #canoe
            if xx <= 60:
                unit = '\U0001F6F6'  
            #racer
            if xx <= 30:
                unit = '\U0001F6A4'  
            #ufo
            if xx <= 3:
                unit = '\U0001F6F8'  
        #seaAnimals
        if x <= 99:
            #fish
            if xx <= 100:
                unit = '\U0001F41F' 
            #tropical
            if xx <= 86:
                unit = '\U0001F420'              
            #puffer
            if xx <= 72:
                unit = '\U0001F421' 
                fish = 0
            #shrimp
            if xx <= 59:
                unit = '\U0001F990'
            #squid
            if xx <= 48:
                unit = '\U0001F991'
            #octopus
            if xx <= 38:
                unit = '\U0001F419'  
            #dolphin
            if xx <= 28:
                unit = '\U0001F42C'   
            #Whale
            if xx <= 19:
                unit = '\U0001F40B'  
            #shark
            if xx <= 11:
                unit = '\U0001F988'  
            #Spout
            if xx <= 5:
                unit = '\U0001F433'  
        #ocean
        if x <= 96:
            unit = '\U0001F30A'
        stringer=str(stringer)+unit 

    stringtext=stringer
    print(stringtext)

    client = tweepy.Client( bearer_token=keys.bearertoken, 
                        consumer_key=keys.consumerkey, 
                        consumer_secret=keys.consumersecret, 
                        access_token=keys.accesstoken, 
                        access_token_secret=keys.accesstokensecret, 
                        wait_on_rate_limit=True)

    response = client.create_tweet(text= stringtext)
    print(response)


def archretweet():
    ##Provides last 5 archillect tweets, pick one to retweet.

    client = tweepy.Client( bearer_token=keys.bearertoken, 
                        consumer_key=keys.consumerkey, 
                        consumer_secret=keys.consumersecret, 
                        access_token=keys.accesstoken, 
                        access_token_secret=keys.accesstokensecret, 
                        wait_on_rate_limit=True)

    #https://tweeterid.com/
    # Archillect Id
    id = '2907774137'

    tweets = client.get_users_tweets(id=id, max_results=5)

    tweetnum = 0

    for tweet in tweets.data:
        print(tweetnum)
        print(str(tweet.data) + '\n')
        tweetnum+=1
    target = int(input("pick a tweet number: ")) 

    response = client.retweet(tweets.data[target].id)
    print(response)

def quickvis():
    #retweets last tweet by visualtweets

    client = tweepy.Client( bearer_token=keys.bearertoken, 
                        consumer_key=keys.consumerkey, 
                        consumer_secret=keys.consumersecret, 
                        access_token=keys.accesstoken, 
                        access_token_secret=keys.accesstokensecret, 
                        wait_on_rate_limit=True)

    #https://tweeterid.com/
    # Visual Tweets id
    id = '1320970636324261889'

    tweets = client.get_users_tweets(id=id, max_results=5)
    response = client.retweet(tweets.data[0].id)
    print(response)
