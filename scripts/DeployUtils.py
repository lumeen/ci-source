import requests
import os
import json
import time

loginUrl = 'https://anypoint.mulesoft.com/accounts/login'
applicationUrl = 'https://anypoint.mulesoft.com/hybrid/api/v1/applications'


def getAuthorizationToken( muleUsername, mulePassword):
  loginResponse = requests.post(loginUrl, data = {'username':muleUsername , 'password': mulePassword})
  return 'Bearer ' + loginResponse.json()['access_token']


def getApplicationId(applicationName, targetId, headers):
  return getApplicationProperty(applicationName, 'id', targetId, headers)

def getApplicationStatus(applicationName, targetId, headers):
  return getApplicationProperty(applicationName, 'lastReportedStatus', targetId, headers)  

def validateResponseCode(apiResponse, responseCode):   
  if apiResponse.status_code != responseCode:
   raise Exception('Error during deploment: ' + apiResponse.json()['message']	)


def getApplicationProperty(applicationName, propertyName, targetId, headers):
  getApplicationsResposne = requests.get(applicationUrl + "?targetId=" + targetId, headers = headers)
  applications = getApplicationsResposne.json()['data']
  applicationProperties = next((x for x in applications if x['name'] == applicationName), None) 
  return applicationProperties[propertyName] if applicationProperties != None else None  

def deployApplication(applicationId, targetId, appName, headers, applicationJar):
  if applicationId == None: 
   response = requests.post(applicationUrl, data={'targetId' :targetId,'artifactName' :appName},   files=applicationJar, headers=headers)
   validateResponseCode(response, 202)
  else:
   response = requests.patch(applicationUrl + "/" + str(applicationId), files=applicationJar, headers=headers)
   validateResponseCode(response, 200)

def validateDeployment(appDeploymentTimeout, appName, targetId, headers):
  print("waliduje")
  timeout = True
  for i in range(0,int(appDeploymentTimeout),1):
    appStatus = getApplicationStatus(appName, targetId, headers)
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
 
