import re
string = input('Enter: ')
result = re.findall(r"\b\w{3,5}\b", string)
print(result)