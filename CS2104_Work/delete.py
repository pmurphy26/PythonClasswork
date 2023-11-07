import requests

url = input("enter your website url here: ")
response = requests.delete(url,
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/json'}
)

