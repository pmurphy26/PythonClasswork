import requests

url = input("enter your website url here: ")
response = requests.get(
    url,
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/json'}
)

json_response = response.json()
for key in json_response:
    print(key["body"])

