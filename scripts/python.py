import requests
import os

url = 'https://anypoint.mulesoft.com/accounts/login'
myobj = {'username': os.environ['muleUsername'], 'password':os.environ['mulePassword']}
x = requests.post(url, data = myobj)

token = x.json()['access_token']
print(token)


url = 'https://anypoint.mulesoft.com/accounts/login'

headers = {'Authorization': 'application/json'}

files = {'file': ('report.csv', 'data to send')}

response = requests.post(url, data={
   'autoStart' :'true',
   'appInfoJson':'{    "domain": "helloo",    "muleVersion": {        "version": "4.2.2"    },    "region": "us-east-1",    "monitoringEnabled": true,    "monitoringAutoRestart": true,    "workers": {        "amount": 1,        "type": {            "name": "Medium",            "weight": 0.2,            "cpu": "0.2 vCore",            "memory": "500 MB memory"        }    },    "loggingNgEnabled": true,    "persistentQueues": false,    "objectStoreV1": false}'
   }, files=files)


pprint(response.json())
print(x.json())

