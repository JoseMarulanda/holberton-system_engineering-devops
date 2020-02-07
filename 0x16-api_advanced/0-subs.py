#!/usr/bin/python3
""" This function queries the Reddit API
and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ This function queries the Reddit API
    and returns the number of subscribers """

    link = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    r = requests.get(link, headers={'User-agent': 'pap'})
    try:
        return(r.json()['data']['subscribers'])
    except:
        return (0)
