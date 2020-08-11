# Where the resust to API is sent

import lambda_function as lmbFunction
import intPersonAPI as personAPI
import urllib.request
import getpass
import urllib.parse
import http.cookiejar
import urllib, base64
from base64 import b64encode
from botocore.vendored import requests
from botocore.vendored.requests.auth import HTTPBasicAuth
from botocore.vendored.requests.auth import _basic_auth_str
from botocore.vendored.requests import Session
import json
import re
import xml.etree.ElementTree as ET
import warnings
import instanceConfiguration as insConfig
import executionCount as exCount

warnings.filterwarnings("ignore")
username = insConfig.userName()
password = insConfig.passWord()


def transferPersonReq(changeEndDateForCashSubscriptions,changePriceForEFTSubscriptions,peCenter,peID,transferCenter,terminateIfUnavailable):
    req = insConfig.reqURL('PersonAPI')
    number = exCount.recordCounter('count')
    numberOfRecords = exCount.fileLineCounter()
    
    headers = {'Authorization':_basic_auth_str(username,password),"Content-Type": "text/xml;charset=UTF-8","SOAPAction": "transferPerson"}
    request = u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v5="http://v5.api.eclub.procard.dk/">
   <soapenv:Header/>
   <soapenv:Body>
      <v5:transferPerson>
         <parameters>
            <changeEndDateForCashSubscriptions>{0}</changeEndDateForCashSubscriptions>
            <changePriceForEFTSubscriptions>{1}</changePriceForEFTSubscriptions>
            <personKey>
               <center>{2}</center>
               <id>{3}</id>
            </personKey>
         <toCenterId>{4}</toCenterId>
         <transferSubscriptionsInfo>
               <terminateIfUnavailable>{5}</terminateIfUnavailable>
         </transferSubscriptionsInfo>
         </parameters>
      </v5:transferPerson>
   </soapenv:Body>
</soapenv:Envelope>""".format(changeEndDateForCashSubscriptions,changePriceForEFTSubscriptions,peCenter,peID,transferCenter,terminateIfUnavailable)

    encoded_request = request.encode('utf-8')
    try:
        #response = requests.post(url=req,headers = headers,data = encoded_request,verify=False)
        #root = ET.fromstring(response.content)
    
        try:
            tPersonCenter = root.findall(".//personId/center")
            tPersonID = root.findall(".//personId/id")
            
            if tPersonCenter == transferCenter:
                lmbFunction.successCounter('count')
                print(str(peCenter)+'p'+str(peID),'->',str(tPersonCenter[0].text)+'p'+str(tPersonID[0].text),'- OK. ',number,'/',numberOfRecords,'records have been processed.')
            else:
                erMessage = root.findall(".//message")
                erCode = root.findall(".//errorCode")
                lmbFunction.errorsCounter('count')
                print(str(peCenter)+'p'+str(peID),'- Failed with code:', erCode[0].text, ' and message ',erMessage[0].text )
                print(number,'/',numberOfRecords,'records have been processed.')
                
        except Exception as e:
            print('This failed...sorry1..')        
            
    except Exception as e:
        print('This failed...sorry2..')
        
    
    if number == numberOfRecords:
        successCount = int(exCount.successCounter('total'))
        errorCount = int(exCount.errorsCounter('total'))
        print('Process completed..\n','Success:',successCount,'Failures:',errorCount)
    
    
    
    
    
    