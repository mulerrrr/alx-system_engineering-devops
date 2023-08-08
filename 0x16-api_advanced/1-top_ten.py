#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of
 the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for
    a given subreddit."""

    header = {"User-Agent": "Jose98"}
    number_hot_posts = {'limit': 10}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=header, params=number_hot_posts)
    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print("None")
