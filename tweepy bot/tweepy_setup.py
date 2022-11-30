import tweepy
import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

keywords = 'covid-19'
limit=100

tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended').items(limit)

columns = ['Date', 'User', 'Tweet']
data = []

for tweety in tweets:
    data.append([tweety.created_at, tweety.user.screen_name, tweety.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)



