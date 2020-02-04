#!/usr/bin/python3
"""
Python script that, using an API, for a given employee ID
returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users/{}'.format(url, sys.argv[1])
    r = requests.get(user)
    json_obj = r.json()
    print("Employee {} is done with tasks".format(json_obj.get('name')),
          end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    r = requests.get(todos)
    tasks = r.json()
    tasks_list = []
    for task in tasks:
        if task.get('completed') is True:
            tasks_list.append(task)

    print("({}/{}):".format(len(tasks_list), len(tasks)))
    for task in tasks_list:
        print("\t {}".format(task.get("title")))
