import json
import os
import urllib
import boto3


def reqURL (intValue):
	interfaceValue = str(intValue)
	instance = 'st-12362'
	environment = 'https://'+instance+'.exerp.qa/api/'
	apiVersion = 'v5'
	req = environment+apiVersion+'/'+interfaceValue+'?wsdl'
	return req 

def userName():
    username = '100emp1'
    return username
    
def passWord():
    password = 'vombat'
    return password