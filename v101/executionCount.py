import json
import os
import urllib
import boto3

success = 0
errors = 0
number = 0
numberOfRecords = 0
	
def recordCounter (numberVal):
	global number
	
	if numberVal =='count':
		number += 1
		return number
	else:
		return number
	
	
def successCounter (successVal):
	global success
	
	if successVal =='count':
		success += 1
		return success
	else:
		return success

def errorsCounter (errorVal):
	global errors

	if errorVal == 'count':
		errors += 1
	else:
		return errors

def fileLineCounter():
    filename = '/tmp/file.csv'
    with open(filename) as f:
        next(f)
        for i, l in enumerate(f):
            pass
    return i + 1