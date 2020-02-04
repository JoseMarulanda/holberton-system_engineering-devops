#!/usr/bin/python3
"""
Python script that, using an API, for a given employee ID
returns information about his/her TODO list progress
"""
import json
import sys
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    userid = sys.argv[1]
    user = '{}users/{}'.format(url, userid)
    r = requests.get(user)
    json_obj = r.json()
    name = json_obj.get('username')

    todos = '{}todos?userId={}'.format(url, userid)
    r = requests.get(todos)
    tasks = r.json()
    tasks_list = []
    for task in tasks:
        dict_task = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": name}
        tasks_list.append(dict_task)

    d_task = {str(userid): tasks_list}
    filename = '{}.json'.format(userid)
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
