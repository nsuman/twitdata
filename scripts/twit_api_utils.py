import json
import os

def save_recent_following_list(username, replace):
    """
    We do not want to be calling the apis often to get the same data.
    This function saves the response to the file so you can 
    read the file later rather than calling the api again. see get_recent_following_list
    function

    Argument:
    username: username
    replace: boolean, replaces the file with current response if True
    """
    if (not replace):
      return
    id = get_userid_from_username(username)
    request_url = get_following_url(id)
    accounts_followed = get_data(request_url)
    filename = '/content/{}.json'.format(username) # edit this line to run locally
    with open(filename, 'a+') as f:
      json.dump(accounts_followed, f)


def get_recent_following_list(username):
  """
  This function returns the latest saved following data. 
  """
  filename = "/content/{}.json".format(username)
  if (not os.path.exists(filename)):
    save_recent_following_list(username, True)

  with open(filename, 'r') as f:
      return json.load(f)

