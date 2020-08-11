import lambda_function as lmbFunction

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


#Cancel booking method. TODO: Move to separate class to clean this page		
def transformInterface(intValue,methValue):
    if intValue == 1:
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 2:
        interfaceString = 'AccountReceivableAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 3:
        interfaceString = 'BookingAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 4:
        interfaceString = 'CenterAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method
        
    elif intValue == 5:
        interfaceString = 'ChildCareAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 6:
        interfaceString = 'ClipcardAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 7:
        interfaceString = 'CompanyAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 8:
        interfaceString = 'CourseAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method
        
    elif intValue == 9:
        interfaceString = 'CrmAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 10:
        interfaceString = 'EmployeeAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 11:
        interfaceString = 'ExtractAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 12:
        interfaceString = 'GiftCardAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method
        
    elif intValue == 13:
        interfaceString = 'PersonAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 14:
        interfaceString = 'ProductAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 15:
        interfaceString = 'QuestionnaireAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 16:
        interfaceString = 'ResourceAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 17:
        interfaceString = 'socialAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 18:
        interfaceString = 'StaffBookingAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method

    elif intValue == 19:
        interfaceString = 'SubscriptionAPI'
        method = eval(interfaceString).transFormMethod(methValue)
        return interfaceString,method