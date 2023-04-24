#!/usr/bin/python3
""" Export to JSON """

import json
import requests
from sys import argv


if __name__ == "__main__":
    """ For a given employee ID, returns information about his/her TODO list
    progress """
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        } for task in todo]}, jsonfile)
