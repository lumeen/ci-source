import requests
import os
import json

def getAuthorizationToken():
  loginResponse = requests.post(loginUrl, data = {'username': os.environ['muleUsername'], 'password':os.environ['mulePassword']})
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
applicationUrl = 'https://anypoint.mulesoft.com/hybrid/api/v1/applications'

envId = os.environ['envId']
orgId = os.environ['orgId']
appName = os.environ['applicationName']
targetId = os.environ['targetId']
files = [f for f in os.listdir('artifact-to-deploy') if (f.endswith('.jar') and f.startswith(appName)) ]
headers = {'Authorization': getAuthorizationToken(), 'X-ANYPNT-ENV-ID': envId, 'X-ANYPNT-ORG-ID': orgId}
applicationJar = {'file': open('artifact-to-deploy/'+ files[0] ,'rb')}
applicationId = getApplicationId()

if applicationId == None: 
   response = requests.post(applicationUrl, data={'targetId' :targetId,'artifactName' :appName},   files=applicationJar, headers=headers)
   validateResponseCode(response, 202)
else:
   response = requests.patch(applicationUrl + "/" + str(applicationId), files=applicationJar, headers=headers)
   validateResponseCode(response, 200)
