import lambda_function as lmbFunction
import reqPersonAPI as reqPersonAPI

def processList(parsedFile,executionMethod):

  if str(executionMethod) == 'createPerson':
    argumentList = []
    argumentList.extend(parsedFile)
    #Send the values of the file to the create person method
    reqPersonAPI.createPerson(*argumentList)
    			
  if str(executionMethod) == 'transferPerson':
      argumentList = []
      argumentList.extend(parsedFile)

      #Send the values of the file to the transer person method
      reqPersonAPI.transferPersonReq(*argumentList)
    
# Decode of ID to determine method
def transFormMethod(methValue):
  if methValue == 1:
    methodString = 'createPerson'
    return methodString
    
  if methValue == 2:
    methodString = 'transferPerson'
    return methodString