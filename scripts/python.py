import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}
print("Hello World!")
x = requests.post(url, data = myobj)

print(x.text)
