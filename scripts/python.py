import requests
import os
import json

def getAuthorizationToken():
  loginResponse = requests.post(loginUrl, data = loginObject)
  return 'Bearer ' + loginResponse.json()['access_token']

def getApplicationId():
  getApplicationsResposne = requests.get(applicationUrl, headers = headers)
  applications = getApplicationsResposne.json()['data']
  applicationProperties = next((x for x in applications if x['name'] == appName), None)
  return applicationProperties['id'] if applicationProperties != None else None

def validateResponseCode(apiResponse, responseCode):   
  if apiResponse.status_code != responseCode:
   raise Exception('Error during deploment: ' + apiResponse.json()['message']	)




loginUrl = 'https://anypoint.mulesoft.com/accounts/login'
applicationUrl = 'https://anypoint.mulesoft.com/hybrid/api/v1//applications'

envId = os.environ['envId']
orgId = os.environ['orgId']
appName = os.environ['applicationName']
targetId = os.environ['targetId']

loginObject = {'username': os.environ['muleUsername'], 'password':os.environ['mulePassword']}
headers = {'Authorization': getAuthorizationToken(), 'X-ANYPNT-ENV-ID': envId, 'X-ANYPNT-ORG-ID': orgId}
files = {'file': open('maven-output/' + appName +'-1.0.0-SNAPSHOT-mule-application.jar','rb')}

applicationId = getApplicationId()
print(applicationId)

if applicationId == None: 
   
   response = requests.post(applicationUrl, data={
   'targetId' :targetId,
   'artifactName' :appName},   
      files=files, headers=headers)
 
   validateResponseCode(response, 202)
else:
  
   response = requests.patch(applicationUrl + "/ds" + str(applicationId),
      files=files, headers=headers)
   
   validateResponseCode(response, 200)
