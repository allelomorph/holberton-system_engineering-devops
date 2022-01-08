# (314) 0x16. API advanced
Foundations > System engineering & DevOps > Scripting

---

### Project author
Tim Britton

### Assignment dates
09-17-2020 to 09-18-2020

### Description
Further practice querying APIs and parsing the JSON results.

### Provided file(s)
* [`0-main.py`](./tests/0-main.py) [`1-main.py`](./tests/1-main.py) [`2-main.py`](./tests/2-main.py) [`100-main.py`](./tests/100-main.py)

---

## Mandatory Tasks

### :white_check_mark: 0. How many subs?
Write a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

Requirements:
* Prototype: `def number_of_subscribers(subreddit)`
* If not a valid subreddit, return 0.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

```bash
$ ./0-main.py programming
756024
$ ./0-main.py this_is_a_fake_subreddit
0
```

File(s): [`0-subs.py`](./0-subs.py)

### :white_check_mark: 1. Top Ten
Write a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and prints the titles of the first 10 hot posts listed for a given subreddit.

Requirements:
* Prototype: `def top_ten(subreddit)`
* If not a valid subreddit, print `None`.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

```bash
$ ./1-main.py programming
Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
HTTPS on Stack Overflow: The End of a Long Road
Spend effort on your Git commits
It's a few years old, but I just discovered this incredibly impressive video of researchers reconstructing sounds from video information alone
From the D Blog: Introspection, Introspection Everywhere
Do MVC like it’s 1979
GitHub is moving to GraphQL for v4 of their API (v3 was a REST API)
Google Bug Bounty - The 5k Error Page
PyCon 2017 Talk Videos
$ ./1-main.py this_is_a_fake_subreddit
None
$ 
```

File(s): [`1-top_ten.py`](./1-top_ten.py)

### :white_check_mark: 2. Recurse it!
Write a *recursive function* that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:
* Prototype: `def recurse(subreddit, hot_list=[])`
* Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.
* If not a valid subreddit, return `None`.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

```bash
$ ./2-main.py programming
932
$ ./2-main.py this_is_a_fake_subreddit
None
```

File(s): [`2-recurse.py`](./2-recurse.py)

## Advanced Tasks

### :white_large_square: 3. Count it!
Write a *recursive function* that queries the [Reddit API](https://www.reddit.com/dev/api/), parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. `Javascript` should count as `javascript`, but `java` should not).

Requirements:
* Prototype: `def count_words(subreddit, word_list)`
* Note: You may change the prototype, but it must be able to be called with just a subreddit supplied and a list of keywords. AKA you can add a counter or anything else, but the function must work without supplying a starting value in the main.
* If `word_list` contains the same word (case-insensitive), the final count should be the sum of each duplicate (example below with `java`)
* Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically (ascending, from A to Z). Words with no matches should be skipped and not printed. Words must be printed in lowercase.
* Results are based on the number of times a keyword appears, not titles it appears in. `java java java` counts as 3 separate occurrences of `java`.
* To make life easier, `java.` or `java!` or `java_` should not count as `java`
* If no posts match or the subreddit is invalid, print nothing.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are NOT following redirects.

Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)

```bash
$ ./100-main.py programming 'react python java javascript scala no_results_for_this_one'
java: 27
javascript: 20
python: 17
react: 17
scala: 4
$ ./100-main.py programming 'JavA java'
java: 54
$ ./100-main.py not_a_valid_subreddit 'python java javascript scala no_results_for_this_one'
$ ./100-main.py not_a_valid_subreddit 'python java'
$ 
```

File(s): [`100-count.py`](./100-count.py)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
