import requests
import os
import json

def getAuthorizationToken():
  loginResponse = requests.post(loginUrl, data = loginObject)
  return 'Bearer ' + loginResponse.json()['access_token']


loginUrl = 'https://anypoint.mulesoft.com/accounts/login'
applicationUrl = 'https://anypoint.mulesoft.com/hybrid/api/v1//applications'

envId = os.environ['envId']
orgId = os.environ['orgId']
appName = os.environ['applicationName']
targetId = os.environ['targetId']

loginObject = {'username': os.environ['muleUsername'], 'password':os.environ['mulePassword']}
headers = {'Authorization': getAuthorizationToken(), 'X-ANYPNT-ENV-ID': envId, 'X-ANYPNT-ORG-ID': orgId}



applicationResposne = requests.get(applicationUrl, headers = headers)

applications = applicationResposne.json()['data']
applicationProperties = next((x for x in applications if x['name'] == 'aaaaaaa'), None)
applicationId =  applicationProperties['id'] if applicationProperties != None else None
files = {'file': open('maven-output/' + appName +'-1.0.0-SNAPSHOT-mule-application.jar','rb')}


if applicationId == None: 
   response = requests.post(applicationUrl, data={
   'targetId' :targetId,
   'artifactName' :appName},   
      files=files, headers=headers)
 
   if response.status_code != 202:
      raise Exception('Error during deploment: ' + response.reason)
else:
   response = requests.patch(applicationUrl + "/" + str(applicationId),
      files=files, headers=headers)
   print(response.status_code)
   if response.status_code != 200:
      raise Exception('Error during deploment: ' + response.reason)

