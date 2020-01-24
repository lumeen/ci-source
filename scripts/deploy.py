import requests
import os
import json
import time
from DeployUtils import getAuthorizationToken, getApplicationId, getApplicationStatus, validateDeployment, validateResponseCode, deployApplication


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

deployApplication(applicationId, targetId, appName, headers)

validateDeployment(appDeploymentTimeout, appName, targetId, headers, applicationJar)

