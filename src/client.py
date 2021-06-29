from requests import put, get, post
import random, string

import json

t = string.ascii_letters
name = []
for i in range(10):
    r = random.choice(t)
    name.extend(r)

url = "http://127.0.0.1:8080"

out = put(url, headers={'content-type': 'application/json'}, json={"title": "".join(name), "description": "blog description","created": "2021-06-27 13:35","author":"User"}).json()

print(out)
