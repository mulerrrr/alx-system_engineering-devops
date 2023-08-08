#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers
for a specigic subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers for subreddit"""

    header = {"User-Agent": "Jose98"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
