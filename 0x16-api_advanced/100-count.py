#!/usr/bin/python3
""" recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords """

import requests


def count_words(subreddit, word_list, after="", word_dict={}):
    """ returns a list containing the titles of all hot articles for a given
    subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/70.0.3538.77 Safari/537.36"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            for word in word_list:
                if word.lower() in post.get("data").get("title").lower():
                    if word.lower() not in word_dict.keys():
                        word_dict[word.lower()] = 1
                    else:
                        word_dict[word.lower()] += 1
        after = response.json().get("data").get("after")
        if after is None:
            if len(word_dict) == 0:
                return
            for key, value in sorted(word_dict.items(),
                                     key=lambda x: (-x[1], x[0])):
                print("{}: {}".format(key, value))
            return
        return count_words(subreddit, word_list, after, word_dict)
    else:
        return None
