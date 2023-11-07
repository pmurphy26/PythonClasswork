import requests

username = input("Enter username:")

url = 'https://posthere.io/6fa2-4057-967d'
myobj = {'somekey': username}

x = requests.post(url, json = myobj)

#print the response text (the content of the requested file):

print(x.text)