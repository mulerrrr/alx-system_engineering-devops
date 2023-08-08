#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns list of hot articles for a given subreddit"""

    header = {"User-Agent": "Jose98"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=header, allow_redirects=False)

    # Establish after fullname
    nxt = None
    if after:
        nxt = {'after': after}
    response = requests.get(url,
                            headers=header, allow_redirects=False, params=nxt)

    if response.status_code != 200:
        return None

    after = response.json().get('data').get('after')
    # append articles for the given subreddit in the current page
    for post in response.json().get('data').get('children'):
        hot_list.append(post.get('data').get('title'))

    # If there are more next pages call recurse function again
    if after:
        return recurse(subreddit, hot_list, after)
    # otherwise return the list with all hot articles for the given subreddit
    return hot_list
