# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 16:47:01 2018

@author: lieby
"""

import config
from twython import Twython, TwythonError
"""
from requests_oauthlib import OAuth1Session
#session = OAuth1Session(config.api_key, config.api_secret, config.access_token, config.token_secret)
#response = session.get("https://api.twitter.com/1.1/trends/place.json?id=23424768")
"""

twitter = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)
        
brasil = twitter.get_place_trends(id=23424768)

try:
    if brasil:
        for trend in brasil[0].get('trends', []):
            print(trend["name"])
except TwythonError as e:
        print(e)
"""
# for each tweet returned from search of #FreeCodeCamp
for tweet in response['statuses']:
    # print each username if needed for debugging
    # print(tweet['user']['screen_name'])
    print(tweet)
    print(tweet["user"]["screen_name"])

    # try to add each user who has tweeted the hashtag to the list

    try:
        twitter.add_list_member(slug='twtapp', owner_screen_name='liebycardoso', screen_name= tweet['user']['screen_name'])
    except TwythonError as e:
        print(e)
"""