import requests
import os
import json
import time

def getAuthorizationToken():
  loginResponse = requests.post(loginUrl, data = {'username': os.environ['muleUsername'], 'password':os.environ['mulePassword']})
  return 'Bearer ' + loginResponse.json()['access_token']

def getApplicationId(applicationName, targetId):
  return getApplicationProperty(applicationName, 'id', targetId)

def getApplicationStatus(applicationName, targetId):
  return getApplicationProperty(applicationName, 'lastReportedStatus', targetId)  

def validateResponseCode(apiResponse, responseCode):   
  if apiResponse.status_code != responseCode:
   raise Exception('Error during deploment: ' + apiResponse.json()['message']	)

def getApplicationProperty(applicationName, propertyName, targetId):
  getApplicationsResposne = requests.get(applicationUrl + "?targetId=" + targetId, headers = headers)
  applications = getApplicationsResposne.json()['data']
  applicationProperties = next((x for x in applications if x['name'] == applicationName), None) 
  return applicationProperties[propertyName] if applicationProperties != None else None

def validateDeployment():
  print("waliduje")
  timeout = True
  for i in range(0,int(appDeploymentTimeout),1):
    appStatus = getApplicationStatus(appName, targetId)
    if appStatus == "DEPLOYMENT_FAILED":
      raise Exception('Error during deployment. Application status: DEPLOYMENT_FAILED')
    elif appStatus == "STARTING":
      time.sleep(1)
      timeout = True
    else:
      timeout = False
      break
    
  if timeout == True:
    raise Exception('Error during deployment: application nas not sterdet before the timeout')  

loginUrl = 'https://anypoint.mulesoft.com/accounts/login'
applicationUrl = 'https://anypoint.mulesoft.com/hybrid/api/v1/applications'

envId = os.environ['envId']
appDeploymentTimeout = os.environ['appDeploymentTimeout']
orgId = os.environ['orgId']
appName = os.environ['applicationName']
targetId = os.environ['targetId']
files = [f for f in os.listdir('artifact-to-deploy') if (f.endswith('.jar') and f.startswith(appName)) ]
headers = {'Authorization': getAuthorizationToken(), 'X-ANYPNT-ENV-ID': envId, 'X-ANYPNT-ORG-ID': orgId}
applicationJar = {'file': open('artifact-to-deploy/'+ files[0] ,'rb')}
applicationId = getApplicationId(appName, targetId)

if applicationId == None: 
   response = requests.post(applicationUrl, data={'targetId' :targetId,'artifactName' :appName},   files=applicationJar, headers=headers)
   validateResponseCode(response, 202)
else:
   response = requests.patch(applicationUrl + "/" + str(applicationId), files=applicationJar, headers=headers)
   validateResponseCode(response, 200)

validateDeployment()

