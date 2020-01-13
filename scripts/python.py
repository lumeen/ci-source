import requests
import os
import json

loginUrl = 'https://anypoint.mulesoft.com/accounts/login'
deploy = 'https://anypoint.mulesoft.com/hybrid/api/v1//applications'

loginObject = {'username': os.environ['muleUsername'], 'password':os.environ['mulePassword']}
x = requests.post(loginUrl, data = loginObject)

token = 'Bearer ' + x.json()['access_token']

url = 'https://anypoint.mulesoft.com/hybrid/api/v1//applications'

headers = {'Authorization': token, 'X-ANYPNT-ENV-ID': '2b38afe9-1e88-411e-82d7-b9376cfab625', 'X-ANYPNT-ORG-ID':'88063e25-29df-47cc-b930-c4c75ee17938'}
files = {'file': open('maven-output/hello-1.0.0-SNAPSHOT-mule-application.jar','rb')}
response = requests.post(deploy, data={
   'targetId' :'2298399',
   'artifactName' :'aaaaaaa'},   
  files=files, headers=headers)

if response.status_code != 202:
   raise Exception('x should not exceed 5. The value of x)




