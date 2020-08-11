import lambda_function as lmbFunction
import os

def executionCompletionNotifier(processID,localFilename):
    # api update lambda
    removeFile(localFilename)
    print('Done! Process ID: ',processID)
    
def executionFailureNotifier(processID):
    removeFile(localFilename)
    print('Execution FailL: ',processID)

def removeFile(localFilename):
    if os.path.exists(localFilename):
        os.remove(localFilename)
        print("Removed the file %s" % localFilename)
    else:
        print("Sorry, file %s does not exist." % localFilename)   
    
    