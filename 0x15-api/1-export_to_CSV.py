#!/usr/bin/python3
"""
Python script that, using an API, for a given employee ID
returns information about his/her TODO list progress
"""
import requests
import sys
import csv


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
        tasks_list.append([userid, name,
                           task.get('completed'),
                           task.get('title')])

    filename = '{}.csv'.format(userid)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in tasks_list:
            employee_writer.writerow(task)
