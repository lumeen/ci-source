import requests
import os
import json

url = 'https://anypoint.mulesoft.com/accounts/login'
myobj = {'username': os.environ['muleUsername'], 'password':os.environ['mulePassword']}
x = requests.post(url, data = myobj)

token = 'Bearer ' + x.json()['access_token']
print(token)


url = 'https://anypoint.mulesoft.com/hybrid/api/v1//applications'
for entry in os.scandir('.'):
        print(entry.name)
headers = {'Authorization': token, 'X-ANYPNT-ENV-ID': '2b38afe9-1e88-411e-82d7-b9376cfab625', 'X-ANYPNT-ORG-ID':'88063e25-29df-47cc-b930-c4c75ee17938'}
files = {'file': ('maven-output/hello-1.0.0-SNAPSHOT-mule-applicationuuu.jar', 'application jar')}
response = requests.post(url, data={
   'targetId' :'2298399',
   'artifactName' :'aaaaaaa'},   
  files=files, headers=headers)


print(response.json())
print(response)
print(response.status_code)
print(response.reason)
print(response.encoding)

