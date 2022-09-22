import requests

BEARER_TOCKEN = "AAAAAAAAAAAAAAAAAAAAADwSOwEAAAAAB37xXGLQZOEUGcss%2FV%2FNimgvklc%3DGmvb3Uf2Fpbqn0ZspTT9MBNwplAvM8ArIb6kTplqIfsV27poIt"

def bearer_oauth(req):
    """
    Adds authorizaton token to request
    """
    req.headers["Authorization"] = f"Bearer {BEARER_TOCKEN}"
    return req

def get_data(url_link):
    """
    Creates a request for the url_link and adds authrization token.
    Arguments:
        url_link -- api url to fetch the data
    """

    res = requests.request("GET", url_link, auth=bearer_oauth)
    contains_data = res.status_code == 200 and 'data' in res.json()

    if (res.headers['x-rate-limit-remaining'] == 0):
      print("Rate Limit Reached. Let's wait 15 minutes before calling this function again")
      return []

    return res.json()['data'] if contains_data else []

def get_data_and_token(url_link):
    res = requests.request("GET", url_link, auth=bearer_oauth)
    print(res.json())
    contains_data = res.status_code == 200 and 'data' in res.json()
    if (contains_data):
        if ('next_token' in res.json()['meta']):
            return (res.json()['data'], res.json()['meta']['next_token'])
        return res.json()['data'], None
    return None