# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:29:53 2018

@author: Ruslan
"""

import urllib.request
from lxml import html


def get_twitter_user_rts_and_favs(screen_name, status_id):
    url = urllib.request.urlopen('https://twitter.com/' + screen_name + '/status/' + status_id)
    root = html.parse(url).getroot()
    num_favs = 0
    fav_users = []

    for ul in root.find_class('stats'):
        for li in ul.cssselect('li'):

            cls_name = li.attrib['class']

            if cls_name.find('favorit') >= 0:
                num_favs = int(li.cssselect('a')[0].attrib['data-tweet-stat-count'])

            elif cls_name.find('avatar') >= 0 or cls_name.find('face-pile') >= 0:#else face-plant

                for users in li.cssselect('a'):
                    if num_favs > 0:
                        num_favs -= 1
                        fav_users.append(users.attrib['data-user-id'])
        
        return fav_users
