#!/usr/bin/python3
"""0x15. API, task 2. Export to JSON
"""
from json import loads, dumps
from requests import get
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]

    user_response = get('https://jsonplaceholder.typicode.com/users/' +
                        user_id)
    username = loads(user_response.text)['username']

    todo_response = get('https://jsonplaceholder.typicode.com/users/' +
                        user_id + '/todos')
    todo_list = loads(todo_response.text)

    user_task_dict = {user_id: []}
    for task in todo_list:
        formatted_task = {}
        formatted_task['task'] = task['title']
        formatted_task['completed'] = task['completed']
        formatted_task['username'] = username
        user_task_dict[user_id].append(formatted_task)

    with open(user_id + '.json', mode='w') as json_file:
        json_file.write(dumps(user_task_dict))
