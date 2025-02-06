# This code is to correct grammar of a string

import requests
import json

url = 'https://api.languagetool.org/v2/check'

to_check = str(input("What text would you like to test?\n"))

data = {
    'text': to_check,
    'language': 'auto'
}

response = requests.post(url, data=data)
result = json.loads(response.text)

print(result)
