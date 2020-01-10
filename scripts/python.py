import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}
print("Hello World!")
x = requests.post(url, data = myobj)
r = requests.get('https://github.com/timeline.json')
print 1
r.text
print 2
print(x.text)
print 3
print(r)
print 4
