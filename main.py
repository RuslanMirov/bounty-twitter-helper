# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 18:21:53 2018

@author: Ruslan
"""

from helpers import Helpers
from twitter_client import TwitterClient 
import config  
 
if __name__ == '__main__':
    
    twitter_client = TwitterClient(config.ID_USER)
    helpers = Helpers()
    
    # Save name from retweets
    list_user = helpers.remove_duplicate(helpers.get_names_from_retweet(twitter_client, config.TWEET_AMOUNT))
    helpers.save("users_retweet", list_user)

    
    # Save id from likes
    list_user2 = helpers.remove_duplicate(helpers.get_names_from_likes(twitter_client, config.ID_USER, config.TWEET_AMOUNT))
    helpers.save("users_likes", list_user2)
    