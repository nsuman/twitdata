import re
import json
from ttp import ttp
from textblob import TextBlob
from nepali_stemmer.stemmer import NepStemmer

from suffix import Nepali_Suffixes
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


def get_words(text):
    words = []
    stemmed_text = nepstem.stem(text)
    delimiters = " ", "|", ":", ";", ".", "-", ",", "!", "?", "''"
    regexPattern = '|'.join(map(re.escape, delimiters))
    words= re.split(regexPattern, stemmed_text) 
    suffix_excluded_list = [x for x in words if x not in Nepali_Suffixes ] 
    words.extend(suffix_excluded_list)

    return words



with open('../tweets_data/ameetdhakal.json', encoding='utf-8') as f:
    f = json.load(f, ensure_ascii=False)
    i = 0
    for tweet in f:
        text = get_text(tweet)
        print(get_words(text))
        i += 1

        if (i > 50):
            break
    
