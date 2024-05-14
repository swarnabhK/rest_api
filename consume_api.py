# get stackoverflow questions by using a get request. Print out the questions and their links
# which haven't been answered yet(answer count is 0), and skip the ones that have been answered atleast once.

import requests
import json

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
data = response.json()
for question in data['items']:
  if question["answer_count"]==0:
    print(question['title'])
    print(question['link'])
  else:
    print("skipped")
  print()