import requests
import os

print (os.environ['muleUsername'])
print (os.environ['mulePassword'])
url = 'https://anypoint.mulesoft.com/accounts/login'
myobj = {'username': os.environ['muleUsername'], 'password':os.environ['mulePassword']}
x = requests.post(url, data = myobj)

print(x.json())

