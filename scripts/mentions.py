import json
from urls import get_mentions_url
from urls import get_mentions_url_with_page
from network import get_data_and_token

list_of_accounts = [
    "SherBDeuba"
]

tweets = []
for acc in list_of_accounts:
    data, token = get_data_and_token(get_mentions_url(acc))
    tweets.extend(data)
    for i in range(12):
        a  = get_data_and_token(get_mentions_url_with_page(acc, token))
        if (a):
            data, token = a
            tweets.extend(data)
        if (not token):
            break
    with open('../mentions_data/{}.json'.format(acc), 'w+', encoding='utf8') as f:
        json.dump(tweets, f, ensure_ascii=False)


