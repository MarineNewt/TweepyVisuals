#!/usr/bin/env python

import tweepy
import keys

# From your app settings page
CONSUMER_KEY = keys.consumerkey
CONSUMER_SECRET = keys.consumersecret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, callback = 'oob')
auth.secure = True
auth_url = auth.get_authorization_url()

print('Please authorize: ' + auth_url)

verifier = input('PIN: ')

auth.get_access_token(verifier)

print ("ACCESS_KEY = " + auth.access_token)
print ("ACCESS_SECRET = " +  auth.access_token_secret)