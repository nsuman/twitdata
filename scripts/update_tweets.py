import tweepy
import json

auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAADwSOwEAAAAAB37xXGLQZOEUGcss%2FV%2FNimgvklc%3DGmvb3Uf2Fpbqn0ZspTT9MBNwplAvM8ArIb6kTplqIfsV27poIt")
api = tweepy.API(auth)

data = [] 
for status in tweepy.Cursor(api.user_timeline, screen_name='@RabindraMishra', tweet_mode="extended").items():
    data.append(status.full_text)

json.dump(data, open('RabindraMishra.json', 'w+', encoding='utf8'), ensure_ascii=False)