import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}
print("Hello World!")
x = requests.post(url, data = myobj)
r = requests.get('https://github.com/timeline.json')
r.text
print(x.text)
print(r)
