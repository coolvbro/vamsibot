import tweepy
import os

consumer_key = os.environ['API_KEY']
consumer_secret = os.environ['API_SECRET_KEY']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

client.create_tweet(text="wig vamsi errip**u 🐍")
print("Tweet sent!")
