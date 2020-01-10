import requests
import os

print (os.environ)
url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}
print("Hello World!")
x = requests.post(url, data = myobj)
r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print (1)
r.text
print (2)

print(x.text)
print (3)

print(r.json())
print (4)

