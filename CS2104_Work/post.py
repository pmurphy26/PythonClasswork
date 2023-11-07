import requests

username = input("Enter username:")

url = 'http://posthere.io/6fa2-4057-967d'
myobj = {'somekey': username}

x = requests.post(url, json = myobj, verify=False)
print(x.text)