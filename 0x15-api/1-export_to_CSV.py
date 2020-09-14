#!/usr/bin/python3
"""0x15. API, task 1. Export to CSV
"""
import csv
from json import loads
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

    with open(user_id + '.csv', mode='w') as csv_file:
        task_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                 quoting=csv.QUOTE_ALL)
        for task in todo_list:
            task_writer.writerow([user_id, username, task['completed'],
                                  task['title']])
