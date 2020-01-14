import requests
import os
import json

loginUrl = 'https://anypoint.mulesoft.com/accounts/login'
applicationUrl = 'https://anypoint.mulesoft.com/hybrid/api/v1//applications'


loginObject = {'username': os.environ['muleUsername'], 'password':os.environ['mulePassword']}
loginResponse = requests.post(loginUrl, data = loginObject)
token = 'Bearer ' + loginResponse.json()['access_token']
headers = {'Authorization': token, 'X-ANYPNT-ENV-ID': '2b38afe9-1e88-411e-82d7-b9376cfab625', 'X-ANYPNT-ORG-ID':'88063e25-29df-47cc-b930-c4c75ee17938'}

applicationResposne = requests.get(applicationUrl, headers = headers)

applications = applicationResposne.json()['data']
applicationProperties = next((x for x in applications if x['name'] == 'aaaaaaa'), None)
applicationId =  applicationProperties['id'] if applicationProperties != None else None
files = {'file': open('maven-output/hello-1.0.0-SNAPSHOT-mule-application.jar','rb')}

print("wchodze1")

if applicationId == None: 
   print("wchodze2")
   response = requests.post(applicationUrl, data={
   'targetId' :'2298399',
   'artifactName' :'aaaaaaa'},   
      files=files, headers=headers)
 
   if response.status_code != 202:
      raise Exception('Error during deploment: ' + response.reason)
else:
   print("wchodze3")
   response = requests.patch(applicationUrl + "/" + str(applicationId),
      files=files, headers=headers)
   print(response.status_code)
   if response.status_code != 202:
      raise Exception('Error during deploment: ' + response.reason)
