#!/usr/bin/python3
"""0x15. API, task 0. Gather data from an API
"""
from json import loads
from requests import get
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]

    user_response = get('https://jsonplaceholder.typicode.com/users/' +
                        user_id)
    user_name = loads(user_response.text)['name']

    todo_response = get('https://jsonplaceholder.typicode.com/users/' +
                        user_id + '/todos')
    todo_list = loads(todo_response.text)

    total_tasks = len(todo_list)
    completed_tasks = []
    for task in todo_list:
        if task['completed'] is True:
            completed_tasks.append(task)

    print('Employee {} is done with tasks({}/{}):'.format(user_name,
                                                          len(completed_tasks),
                                                          total_tasks))
    for task in completed_tasks:
        print('\t {}'.format(task['title']))
