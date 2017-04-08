from EmailHeaders import Header
from EmailBody import Body


#-------IMPORTANT Reference-----------------
#---List of Email Client Software-----------
#https://en.wikipedia.org/wiki/Comparison_of_email_clients

class emailAnalyzer:
    f = open("D:\\Srihari\\Spam filtering\\20021010_spam.tar\\0018.259154a52bc55dcae491cfded60a5cd2", 'r')

    def __init__(self):
        #Calling EmailHeaders class
        first = Header()

        #Calling EmailBody class
        second = Body()
