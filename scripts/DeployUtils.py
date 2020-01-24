import requests
import os
import json
import time

loginUrl = 'https://anypoint.mulesoft.com/accounts/login'

def getAuthorizationToken(muleUsername, mulePassword):
  loginResponse = requests.post(loginUrl, data = {'username':muleUsername , 'password': mulePassword})
  return 'Bearer ' + loginResponse.json()['access_token']
