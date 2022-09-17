import json
import tweepy

auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAADwSOwEAAAAAB37xXGLQZOEUGcss%2FV%2FNimgvklc%3DGmvb3Uf2Fpbqn0ZspTT9MBNwplAvM8ArIb6kTplqIfsV27poIt")
api = tweepy.API(auth)

def get_user_timeline(username):
    cursor = tweepy.Cursor(
        api.user_timeline, 
        screen_name=username, 
        tweet_mode="extended"
    )
    return [tweet.full_text for tweet in cursor.items()]

def save_timeline(username):
    timeline = get_user_timeline(username)
    f = open(f'../tweets_data/{username}.json', 'w+', encoding='utf8')
    json.dump(timeline, f, ensure_ascii=False)
    f.close()


journalists = [
    "sudheerktm",
    "tikaramyatri",
    "gbudhathoki",
    "Bijaysspaudel",
    "basantabasnet",
    "Umesh_Chauhan",
    "BhagirathYogi",
    "ameetdhakal",
    "salokya",
    "gunaraj",
    "akhileshU",
    "Teknarayan_",
    "kirannepal",
    "DahalTbd",
    "Vijaykumarko",
    "kundadixit",
    "SanjeevSatgainy"
]


for acc in journalists:
    save_timeline(acc)