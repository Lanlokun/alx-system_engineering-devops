#!/usr/bin/python3
""" Export to CSV """

import csv
import requests
from sys import argv


if __name__ == "__main__":
    """ For a given employee ID, returns information about his/her TODO list
    progress """
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([user_id, user.get("username"),
                             task.get("completed"), task.get("title")])
