import os
import json

from urls import get_usernames_url
from network import get_data

USERS_LOCATION = '../users/'
categories = os.listdir(USERS_LOCATION)
profile_data = []
for i in categories:
    def my_func(a):
        data = {}
        data['id'] = a['id']
        data['followers_count'] = a['public_metrics']['followers_count']
        data['following_count'] = a['public_metrics']['following_count']
        data['tweet_count'] = a['public_metrics']['tweet_count']
        data['username'] = a['username']
        data['name'] = a['name']
        data['profile_image_url'] = a['profile_image_url']
        data['category'] = i[:-5]
        return data
    user_list = json.load(open(os.path.join(USERS_LOCATION, i)))
    profile_data.extend(list(map(my_func, get_data(get_usernames_url(user_list)))))

profile_file = open('../users_profile/users_profile.json', 'w+')
json.dump(profile_data, profile_file)
profile_file.close()


username_to_userid = {i['username']: i['id'] for i in profile_data}
file = open('../users_profile/username_to_userid.json', 'w+')
json.dump(username_to_userid, file)
file.close()

def get_all_user_names():
    usernames = []
    for category in categories:
        category_users = json.load(open(os.path.join(USERS_LOCATION, category)))
        usernames.extend(category_users)
    return usernames 

