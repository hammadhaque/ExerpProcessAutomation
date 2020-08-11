import csv
import json
import datetime as dt
import boto3
import os
import lambda_function as lmbFunction

datestamp = dt.datetime.now().strftime("%Y/%m/%d")
timestamp = dt.datetime.now().strftime("%s")

filename_json = "/tmp/file_{ts}.json".format(ts=timestamp)
filename_csv = "/tmp/file_{ts}.csv".format(ts=timestamp)

def processLine (line):
	line = line
	line = line.split(",")
	data = []
	#csv_file = csv.DictReader(line)
	dataPre = list(line)
	dataPreII = json.dumps(dataPre)
	data = json.loads(dataPreII)
	return data

def readFile (response,filetype):
    if filetype == 'json':
        text = response["Body"].read().decode()
        data = json.loads(text)
        print('Complete read of JSON')
        return data
        
    elif filetype == 'csv':
        csvcontent = response['Body'].read().decode('utf-8-sig').split('\n')
        data = []
        csv_file = csv.DictReader(csvcontent)
        dataPre = list(csv_file)
        dataPreII = json.dumps(dataPre)
        data = json.loads(dataPreII)
        print('Complete read of CSV')
        
        return data

       
       
        
        