#!/usr/bin/python3
"""0x15. API, task 3. Dictionary of list of dictionaries
"""
from json import loads, dumps
from requests import get
from sys import argv


if __name__ == "__main__":
    users_response = get('https://jsonplaceholder.typicode.com/users')
    user_list = loads(users_response.text)

    todos_response = get('https://jsonplaceholder.typicode.com/todos')
    task_list = loads(todos_response.text)

    user_task_dict = {}
    for user in user_list:
        user_id = user['id']
        username = user['username']
        user_task_dict[user_id] = []
        gen = (task for task in task_list
               if task['userId'] == user_id)
        for task in gen:
            formatted_task = {}
            formatted_task['task'] = task['title']
            formatted_task['completed'] = task['completed']
            formatted_task['username'] = username
            user_task_dict[user_id].append(formatted_task)

    with open('todo_all_employees.json', mode='w') as json_file:
        json_file.write(dumps(user_task_dict))
