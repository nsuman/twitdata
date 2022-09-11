import json
from ttp import ttp
from textblob import TextBlob
from nepali_stemmer.stemmer import NepStemmer

from googletrans import Translator
translator = Translator()

def translate(text):
    return translator.translate(text).text

def get_sentiment(text):
    blob = TextBlob(text)
    return (blob.sentiment.polarity, blob.sentiment.subjectivity)

nepstem = NepStemmer()
parser = ttp.Parser(include_spans=True)

def remove_category(tweet, c):
    cpy = tweet[:]
    results = parser.parse(cpy)

    if (getattr(results, c) is not None):
        for i in getattr(results, c):
            span = i[1]
            for j in range(span[0], span[1]):
                cpy = cpy[0: j] + ' ' + cpy[j+1:]
        
    return cpy

to_parse = ['tags', 'urls', 'users', 'lists']

def get_text(tweet):
    copy_tweet = tweet[:]
    for category in to_parse:
        copy_tweet = remove_category(copy_tweet, category)
    return " ".join(copy_tweet.split())
    
with open('../tweets_data/BalenShah.json', encoding='utf8',  errors="ignore") as f:
    f = json.load(f)
    i = 0
    for tweet in f:
        text = get_text(tweet)
        sentiment = get_sentiment(translate(text))
        print(text[:100], sentiment)
        i += 1
        if i == 50:
            break
    




    
