__author__ = 'Chris'

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import Listener
import Organizer
#To keep keys secret, left them in a keys.txt file and read them to vars
with open('keys.txt', 'r') as f:
    consumer_key = f.readline().rstrip()
    consumer_secret = f.readline().rstrip()
    access_token = f.readline().rstrip()
    access_secret = f.readline().rstrip()

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

MyListener = Listener.MyListener()

twitter_stream = Stream(auth, MyListener)

twitter_stream.filter(track=['#python'])

