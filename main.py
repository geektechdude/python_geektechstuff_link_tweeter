#!/usr/bin/python3
# geektechstuff Python Link Tweeter

# libraries to import
import random
from twython import Twython

# auth file contains all the Twitter details for account
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# setting up Twitter
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def random_line(filename):
    lines = open(filename).read().splitlines()
    return random.choice(lines)

def tweet_to_send():
    tweet_to_send = random_line('path_to_file')
    tweet_to_send_str = str(tweet_to_send)
    twitter.update_status(status=tweet_to_send_str)
    return()

tweet_to_send()