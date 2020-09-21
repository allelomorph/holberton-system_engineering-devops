#!/usr/bin/python3
""" 0x16. API advanced, task 3. Count it!
"""
from re import findall, IGNORECASE
from requests import get


def count_words(subreddit, word_list, word_totals={}, after=''):
    """ Tallies appearances of search terms in all "hot" post titles for a
    given subreddit.

        Recursively queries Reddit API, one page per frame, to parse titles of
    all "hot" posts and count occurances of each word in a given list of
    search terms. Once finished, prints all non-zero totals sotrted first in
    descending order by count, and then in alphabetic order.

    Args:
        subreddit (str): subreddit to query
        word_list (list): list of words to search for in titles of all posts
           in "hot"
        word_totals (dict): running total of search term occurances prior to
            current page/frame
        after (str): API name for last post in previous page

    Return:
        dict of running word totals from titles in all API pages parsed in
    current recursion frame and those below
    """
    limit = 100
    # (adding request parameter raw_json deactivates default ampersand escape)
    url = 'https://www.reddit.com/r/{}/hot.json?raw_json=1&after={}&limit={}'
    response = get(url.format(subreddit, after, limit),
                   headers={'User-Agent': 'allelomorph-app2'})

    # 404 or other error, or no search terms
    if response.status_code != 200 or len(word_list) == 0:
        return

    regex = '^{}$|^{} +| +{} +| +{}$'
    word_count = dict.fromkeys([word.lower() for word in word_list], 0)
    current_page_list = response.json().get('data').get('children', [])

    # search titles in current page for terms
    for post in current_page_list:
        title = post.get('data').get('title', '')
        for word in word_list:
            count = len(findall(regex.format(word, word, word, word),
                                title, IGNORECASE))
            word_count[word.lower()] += count

    # update totals
    for key, value in word_count.items():
        if key in word_totals:
            word_totals[key] += value
        else:
            word_totals[key] = value

    # last page reached, print totals
    if len(current_page_list) < limit:
        for item in sorted(word_totals.items(),
                           key=lambda item: (-item[1], item[0])):
            if item[1] > 0:
                print('{}: {}'.format(item[0], item[1]))
        return

    # still more titles to parse, recurse to next frame
    after = current_page_list[-1].get('data').get('name', '')
    return count_words(subreddit, word_list, word_totals, after)
