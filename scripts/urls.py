import json

USERS_FIELDS = "id,name,public_metrics,url,username,verified,profile_image_url"

TWEET_FIELDS = "text,context_annotations,public_metrics,in_reply_to_user_id"

api_root = "https://api.twitter.com/2"
user_options = "user.fields={}".format(USERS_FIELDS)
tweet_options = "tweet.fields={}".format(TWEET_FIELDS)

def get_following_url(userid):
    """
    This function creates the url of the request to get the following list 
    for userid.
    """
    return "{}/users/{}/following?{}&{}max_results=1000".format(api_root, userid, user_options)


def get_timeline_url(userid):
    """
    This function returns the url for last 100 tweets of the userid
    """

    return "{}/users/{}/tweets?max_results=100&{}".format(api_root, userid, tweet_options)

def get_usernames_url(usernames):
    users_list = ','.join(usernames)
    return "{}/users/by?usernames={}&{}".format(api_root, users_list, user_options)


def get_mentions_url_with_page(username, next_token):
    username_to_userid = json.load(open('../users_profile/username_to_userid.json'))
    id = username_to_userid[username]
    return "{}/users/{}/mentions?max_results=100&tweet.fields=id,text,author_id&user.fields=id,name,username&pagination_token={}".format(api_root, id, next_token)

def get_mentions_url(username):
    username_to_userid = json.load(open('../users_profile/username_to_userid.json'))
    id = username_to_userid[username]
    return "{}/users/{}/mentions?max_results=100&tweet.fields=id,text,author_id&user.fields=id,name,username".format(api_root, id)