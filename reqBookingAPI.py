# Where the resust to API is sent
import lambda_function as lmbFunction
import intBookingAPI as bookingAPI
import urllib.request
import getpass
import urllib.parse
from xml.dom import minidom
import http.cookiejar
import urllib, base64
from base64 import b64encode
from botocore.vendored import requests
from botocore.vendored.requests.auth import HTTPBasicAuth
from botocore.vendored.requests.auth import _basic_auth_str
import json
import re
import xml.etree.ElementTree as ET
import warnings
import executionCount as exCount
import instanceConfiguration as insConfig

warnings.filterwarnings("ignore")
username = insConfig.userName()
password = insConfig.passWord()


def cancelBookingReq(bookingCenter, bookingID, notifyParticipants, notifyStaff, message):
    req = insConfig.reqURL('BookingAPI')
    number = exCount.recordCounter('count')
    numberOfRecords = exCount.fileLineCounter()
    
    headers = {'Authorization':_basic_auth_str(username,password),"Content-Type": "text/xml;charset=UTF-8","SOAPAction": "cancelBooking"}
    request = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v5="http://v5.api.eclub.procard.dk/">
   <soapenv:Header/>
   <soapenv:Body>
      <v5:cancelBooking>
         <bookingKey>
            <center>{0}</center>
            <id>{1}</id>
         </bookingKey>
         <notifyParticipants>{2}</notifyParticipants>
         <notifyStaff>{3}</notifyStaff>
         <message>{4}</message>
      </v5:cancelBooking>
   </soapenv:Body>
</soapenv:Envelope>""".format(bookingCenter,bookingID,notifyParticipants,notifyStaff,message)
    encoded_request = request.encode('utf-8')

    #response = requests.post(url=req,headers = headers,data = encoded_request,verify=False)
    #root = ET.fromstring(response.content)
    try:
        erMessage = root.findall(".//errorMessage")
        erCode = root.findall(".//errorCode")
        exCount.errorsCounter('count')
        
        print(str(bookingCenter)+'book'+str(bookingID),'- Failed with code:', erCode[0].text, ' and message ',erMessage[0].text )
        print(number,'/',numberOfRecords,'records have been processed.')
        
    except Exception as e:
        exCount.successCounter('count')
        print(str(bookingCenter)+'book'+str(bookingID),'- OK.',number,'/',numberOfRecords,'records have been processed.')
    
    if number == numberOfRecords:
        successCount = int(exCount.successCounter('total'))
        errorCount = int(exCount.errorsCounter('total'))
        print('Process completed..\n','Success:',successCount,'Failures:',errorCount)
    
        

def cancelPersonParticipation(partCenter, partID, peCenter, peID, UserInterfaceType, sendCancelMessage):
    global success
    global errors
    
    req = insConfig.reqURL('BookingAPI')
    print('We will point to: ',req)
    
    headers = {'Authorization':_basic_auth_str(username,password),"Content-Type": "text/xml;charset=UTF-8","SOAPAction": "cancelPersonParticipation"}
    request = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v5="http://v5.api.eclub.procard.dk/">
   <soapenv:Header/>
   <soapenv:Body>
      <v5:cancelPersonParticipation>
         <participationId>
            <center>{0}</center>
            <id>{1}</id>
         </participationId>
         <personKey>
            <center>{2}</center>
            <id>{3}</id>
         </personKey>
         <userInterfaceType>{4}</userInterfaceType>
         <sendCancelMessage>{5}</sendCancelMessage>
      </v5:cancelPersonParticipation>
   </soapenv:Body>
</soapenv:Envelope>""".format(partCenter, partID, peCenter, peID, UserInterfaceType, sendCancelMessage,req)

    encoded_request = request.encode('utf-8')
    response = requests.post(url=req,headers = headers,data = encoded_request,verify=False)
    print (response.content)

    print (str(partCenter)+'part'+str(partID)," had cancellation requests sent to endpoint ",req)
    
    
    
    
    
    