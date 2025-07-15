# twitterbot_post_tweet.py

import tweepy
from credentials import *

# Step 1: Authenticate
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Step 2: Post a tweet
try:
    tweet_text = "Hello Twitter! 🐦 This is my working bot using Tweepy and Python. #PythonBot"
    api.update_status(tweet_text)
    print("✅ Tweet posted successfully!")
except Exception as e:
    print("❌ Error:", e)
