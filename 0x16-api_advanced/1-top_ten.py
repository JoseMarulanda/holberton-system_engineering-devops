#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit. """
import requests


def top_ten(subreddit):
    """ queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit. """

    link = "https://www.reddit.com//r/" + subreddit + "/hot.json"
    r = requests.get(link, headers={'User-agent': 'jose'},
                     allow_redirects=False)
    try:
        for i in range(0, 10):
            print (r.json()['data']['children'][i]['data']['title'])
    except Exception as err:
        print("None")
