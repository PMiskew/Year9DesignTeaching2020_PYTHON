#https://realpython.com/python-json/
#https://jsonplaceholder.typicode.com/posts
#

import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
todos = json.loads(response.text)

print(todos[3]["id"])