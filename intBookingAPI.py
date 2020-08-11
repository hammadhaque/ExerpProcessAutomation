import lambda_function as lmbFunction
import reqBookingAPI as reqBookingAPI
from collections import OrderedDict
from multiprocessing.pool import ThreadPool
import threading
from time import sleep
import random
import logging


def processList(parsedFile,executionMethod):
  if str(executionMethod) == 'cancelBooking':
    argumentList = []
    argumentList.extend(parsedFile)
    reqBookingAPI.cancelBookingReq(*argumentList)

  if str(executionMethod) == 'cancelPersonParticipation':
    argumentList = []
    argumentList.extend(parsedFile)
    reqBookingAPI.cancelPersonParticipation(*argumentList)


# Decode of ID to determine method
def transFormMethod(methValue):
  if methValue == 1:
    methodString = 'cancelBooking'
    return methodString
    
  if methValue == 2:
    methodString = 'cancelPersonParticipation'
    return methodString