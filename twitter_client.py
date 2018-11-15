# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 15:16:31 2018

@author: Ruslan
"""
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
import twitter_credentials

# # # # TWITTER CLIENT # # # #
class TwitterClient():
    
    def __init__(self, twitter_user):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth, wait_on_rate_limit=True)
        self.twitter_user = twitter_user
    
    def get_retweets(self, _id):
        ret = self.twitter_client.retweets(_id, 100)
        retweets_list = []
        for retweets in ret:
            retweets_list.append(retweets.user.screen_name)
        return retweets_list
    
    def get_tweets_id(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet.id)
        return home_timeline_tweets
    
# # # # TWITTER AUTHENTICATER # # # #
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth