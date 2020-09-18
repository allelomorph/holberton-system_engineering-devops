#!/usr/bin/python3
""" 0x16. API advanced, task 3. Count it!
"""
from re import findall
from requests import get


def word_count_sort(item):
    """ Sorts dict items first by value in descending order, then by key in
    ascending alpha order.
    """
    word = item[0]
    count = item[1]
    return (-count, word)


def count_words(subreddit, word_list, word_totals={}, after=''):
    """ Recursively queries Reddit API, one page per frame, to parse titles of
    all "hot" posts to tally occurances of each word in a given list of
    search terms.

    Args:
        subreddit (str): subreddit to query
        word_list (list): list of words to search for in titles of all posts
    in "hot"

    Return:
        `hot_list` with the current API page/recursion frame's list appended
    """
    limit = 100
    # print(after, sum(word_totals.values()))
    # (adding request parameter raw_json deactivates default ampersand escape)
    url = 'https://www.reddit.com/r/{}/hot.json?raw_json=1&after={}&limit={}'
    response = get(url.format(subreddit, after, limit),
                   headers={'User-Agent': 'allelomorph-app2'})

    # 404 or other error, or no search terms
    if response.status_code != 200 or len(word_list) == 0:
        print()
        return

    regex = '^{} +| +{} +| +{}$'
    word_count = dict.fromkeys(word_list, 0)
    current_page_list = response.json().get('data').get('children', [])

    # search titles in current page for terms
    for post in current_page_list:
        title = post.get('data').get('title', '')
        for word in word_list:
            count = len(findall(regex.format(word, word, word), title))
            # if count > 0:
            #     print(title, word, count)
            word_count[word] += count

    # update grand totals
    for key, value in word_count.items():
        if key in word_totals:
            word_totals[key] += value
        else:
            word_totals[key] = value

    # last page reached, print totals
    if len(current_page_list) < limit:
        for item in sorted(word_totals.items(), key=word_count_sort):
            # key=lambda item: (-item[1], item[0])):
            if item[1] > 0:
                print('{}: {}'.format(item[0], item[1]))
        if sum(word_totals.values()) == 0:
            print()
        return

    after = current_page_list[-1].get('data').get('name', '')
    return count_words(subreddit, word_list, word_totals, after)
