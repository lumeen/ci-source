import requests
import os
import json
import time
from DeployUtils import getAuthorizationToken, getApplicationId, getApplicationStatus, validateDeployment, validateResponseCode

applicationUrl = 'https://anypoint.mulesoft.com/hybrid/api/v1/applications'


envId = os.environ['envId']
muleusername = os.environ['muleUsername']
mulepassword = os.environ['mulePassword']
appDeploymentTimeout = os.environ['appDeploymentTimeout']
orgId = os.environ['orgId']
appName = os.environ['applicationName']
targetId = os.environ['targetId']

files = [f for f in os.listdir('artifact-to-deploy') if (f.endswith('.jar') and f.startswith(appName)) ]

headers = {'Authorization': getAuthorizationToken(muleusername, mulepassword), 'X-ANYPNT-ENV-ID': envId, 'X-ANYPNT-ORG-ID': orgId}

applicationJar = {'file': open('artifact-to-deploy/'+ files[0] ,'rb')}

applicationId = getApplicationId(appName, targetId, headers)

if applicationId == None: 
   response = requests.post(applicationUrl, data={'targetId' :targetId,'artifactName' :appName},   files=applicationJar, headers=headers)
   validateResponseCode(response, 202)
else:
   response = requests.patch(applicationUrl + "/" + str(applicationId), files=applicationJar, headers=headers)
   validateResponseCode(response, 200)

validateDeployment(appDeploymentTimeout, appName, targetId, headers)

