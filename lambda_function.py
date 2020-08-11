import json
import os
import urllib
import boto3
import datetime as dt
import filereader as filereader
#import intAccessAPI as AccessAPI
#import intAccountReceivableAPI as AccountReceivableAPI
import intBookingAPI as BookingAPI
#import intCenterAPI as CenterAPI
#import intChildCareAPI as ChildCareAPI
#import intClipcardAPI as ClipcardAPI
#import intCompanyAPI as CompanyAPI
#import intCourseAPI as CourseAPI
#import intCrmAPI as CrmAPI
#import intEmployeeAPI as EmployeeAPI
#import intExtractAPI as ExtractAPI
#import intGiftCardAPI as GiftCardAPI
import intPersonAPI as PersonAPI
#import intProductAPI as ProductAPI
#import intQuestionnaireAPI as QuestionnaireAPI
#import intResourceAPI as ResourceAPI
#import intsocialAPI as socialAPI
#import intStaffBookingAPI as StaffBookingAPI
#import intSubscriptionAPI as SubscriptionAPI
import interfaceTransform as intTrans
import schedulerNotify as notifySchedule
import tempfile as tmpfile
import csv
import instanceConfiguration as insConfig

print('Loading function')

# TODO
# Read type of file that is returned, only process accepted files (JSON, XLSX, CSV)
# Dynamic file reading of contents. Bookings expects bookings etc
# Multiprocessing: Should we take 1 file into a stage, split it up, 
#	then drop each into the main directory to be processed? Or code multiprocessing.
# Wrap up coding other accepted API classes
# Documentation


s3 = boto3.client('s3')


datestamp = dt.datetime.now().strftime("%Y/%m/%d")
timestamp = dt.datetime.now().strftime("%s")
    
filename_json = "/tmp/file_{ts}.json".format(ts=timestamp)
filename_csv = "/tmp/file_{ts}.csv".format(ts=timestamp)


def lambda_handler(event, context):
	#1 - Get the bucket name
	bucket = event['Records'][0]['s3']['bucket']['name']

	#2 - Get the file/key name
	key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
	
	
	#3 - Parse the file name and store as variables
	fileName = key.split("_")
	processID = str(fileName[0]).replace('PROD/','')
	processID = int(processID)
	executionInterface = int(fileName[1])
	fexecutionMethod= int(fileName[2])
	extractFileName = fileName[3]
	executionDate = fileName[4]
	file = key.split(".")
	filetype = file[1]
	
	#4 - Check
	print('File extension: ',filetype.upper())
	
	localFilename = '/tmp/file.csv'
	s3.download_file(bucket, key, localFilename)
	
	
	#5 - Conditional check for files we accept
	if  filetype == 'json' or filetype =='csv':
		print(filetype.upper(), 'accepted. We will proceed..')
	
		try:
			
			#6 - Map the interface & Mehtod ID from file name to get right class
			interfaceArray = []
			interfaceArray.extend(intTrans.transformInterface(executionInterface,fexecutionMethod))
			intValue = interfaceArray[0]
			intMethod = interfaceArray[1]
	
			#ex Print out for logging purposes
			print('Interface & Method: '+intValue+';'+intMethod)

			#7 - Set value of method to be passed:
			executionMethod = (intMethod)
			print('Will use '+ str(intValue) + ' as interface and the method ' + str(executionMethod)+ ' as determined by filename..')		
			
			#8 - Build the endpoint URL
			req = insConfig.reqURL(intValue)
			print('API Endpoint is: ',req)
			
			#9 - Ship the file contents to the method which will handle the transaction
			apiInterface = eval(intValue)

			#10 - Fetch the file from S3
			response = s3.get_object(Bucket=bucket, Key=key)
			
			#11 - Parse file contents and store as dictionary
			#parsedFile = filereader.readFile(response,filetype)
			
			print ()
			with open(localFilename) as f:
				next(f)
				for line in f:
					parsedFile = filereader.processLine(line)
					apiInterface.processList(parsedFile,executionMethod)
			
			#12 - Failure or Success response
			return notifySchedule.executionCompletionNotifier(processID,localFilename)

		except Exception as e:
			print(e)
			raise e
		
	else:
		#13 - We don't accept the file supplied so we reject
		print('We do not accpt ',filetype,' at this time :(')
		
