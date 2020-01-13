import requests
import os
import json

url = 'https://anypoint.mulesoft.com/accounts/login'
myobj = {'username': os.environ['muleUsername'], 'password':os.environ['mulePassword']}
x = requests.post(url, data = myobj)

token = 'Bearer ' + x.json()['access_token']
print(token)


url = 'https://anypoint.mulesoft.com/cloudhub/api/v2/applications/'

headers = {'Authorization': token, 'X-ANYPNT-ENV-ID': '2b38afe9-1e88-411e-82d7-b9376cfab625',  'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'}
files = {'file': ('maven-output/hello-1.0.0-SNAPSHOT-mule-application.jar', 'data to send')}
cwd = os.getcwd()
print(cwd)
for entry in os.scandir('maven-output'):
        print(entry.name)
response = requests.post(url, data={
   'autoStart' :'true',
   'appInfoJson':'{    "domain": "helloo",    "muleVersion": {        "version": "4.2.2"    },    "region": "us-east-1",    "monitoringEnabled": true,    "monitoringAutoRestart": true,    "workers": {        "amount": 1,        "type": {            "name": "Medium",            "weight": 0.2,            "cpu": "0.2 vCore",            "memory": "500 MB memory"        }    },    "loggingNgEnabled": true,    "persistentQueues": false,    "objectStoreV1": false}'
   }, files=files, headers=headers)
print(response.json())
print(response)
print(response.status_code)
print(response.reason)
print(response.encoding)



