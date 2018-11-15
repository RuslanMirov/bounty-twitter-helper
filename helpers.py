# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:20:01 2018

@author: Ruslan
"""
from parse_user_likes import get_twitter_user_rts_and_favs

# # # # HELPERS for parse, sort, delete dublicate and save # # # #  
class Helpers():
    
    def save(self, namefile, content):
        with open(namefile + '.txt', 'w') as f:
           for item in content:
              f.write("%s\n" % item)

    def get_names_from_retweet(self, twitter_client, tweets_amount):
        id_tweet_list = (twitter_client.get_tweets_id(tweets_amount))
        user_list = []
        pattern = []
    
        for id_t in id_tweet_list:
            if id_t != pattern:
               user_list = user_list + twitter_client.get_retweets(id_t)
        return user_list
    
    def get_names_from_likes(self, twitter_client, url, tweets_amount):
        id_tweet_list = (twitter_client.get_tweets_id(tweets_amount))
        user_list = []
        pattern = []
    
        for id_t in id_tweet_list:
            if id_t != pattern:
               user_list = user_list + get_twitter_user_rts_and_favs(url, str(id_t))
       
        return user_list
        
              
    def remove_duplicate(self, sort_list):
        final_list = []
        for i in sort_list:
           if i not in final_list:
              final_list.append(i)
        return final_list
        