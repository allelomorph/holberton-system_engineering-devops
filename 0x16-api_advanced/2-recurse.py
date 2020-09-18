#!/usr/bin/python3
""" 0x16. API advanced, task 2. Recurse it!
"""
from requests import get


def recurse(subreddit, hot_list=[]):
    """ Recursively queries Reddit API, one page per frame, to compile list of
    all "hot" posts for a given subreddit.

    Args:
        subreddit (str): subreddit to query
        hot_list (list): list of dictionaries representing posts in "hot",
            compiled from lower frames in the stack

    Return:
        `hot_list` with the current API page/recursion frame's list appended
    """
    limit = 100
    after = hot_list[-1].get('data').get('name', '') if len(hot_list) else ''
    # adding request parameter `raw_json` deactivates default ampersand escape
    url = 'https://www.reddit.com/r/{}/hot.json?raw_json=1&after={}&limit={}'
    response = get(url.format(subreddit, after, limit),
                   headers={'User-Agent': 'allelomorph-app2'})
    if response.status_code != 200:
        return None
    current_page_list = response.json().get('data').get('children', [])
    if len(current_page_list) < limit:
        return hot_list + current_page_list
    return recurse(subreddit, hot_list + current_page_list)
