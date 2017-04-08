import numpy
import csv
import re
#from EmailGo import emailAnalyzer
from EmailHeaders import Header
import email
import RabinKarp
import Spam_BoW
from email.mime.multipart import MIMEMultipart
from email.parser import HeaderParser
from mailbox import mbox

class Body:
    blankline_pos = 0
    i = 0
    line = ''
    message_body = []
    url_presence = 0
    q = 101
    retSpamword = []
    flag_spmcount = 0
    mess_count = 0

    f = open("D:\\Srihari\\Spam filtering\\20021010_spam.tar\\0018.259154a52bc55dcae491cfded60a5cd2",'r')

    '''
    Subject part in EmailHeaders.py
    '''

    for i, line in enumerate(f,1):
        if line in ['\n', '\r\n']:
            print('lineno', i)
            break

    print('global i', i)

    for i, line in enumerate(f):
        message_body.append(line)
        #----------1----------------------------------------
        #---URL presence Block
        #Check for URLS in Message body
        chk_urls = re.search(r"(http://[^ ]+)", line)
        if chk_urls:
            url_presence += 1
            #print('URL present')
        else:
            url_presence += 0
            #print('URL not present')

    #----------2----------------------------------------
    #Spam words -- Bag of Words
    #Joining the contents of message
    mess_body = ''.join(message_body)
    print('chk2', message_body[0:])
    print('chk1', mess_body)
    #To remove \n from the string
    mess_body = mess_body.replace('\n', ' ')

    #for mess in message_body:
    for spam_bw in Spam_BoW.Spam_words:
        retSpam = RabinKarp.rbk(mess_body, spam_bw, q)
        retSpamword.append(retSpam)
        print('spam chk', retSpam)

    print('message body',mess_body)
    print('spam array', retSpamword[0:])

    for ispam in retSpamword:
        if ispam == 1:
            flag_spmcount += 1

    #----------3----------------------------------------
    #-----Count of the Email Body
    mess_count = len(mess_body.split())
    print('Number of words in Message body', mess_count)

    #Final Message body features
    print('url presence', url_presence)
    print('flag count', flag_spmcount)
    print('Number of words in Message body', mess_count)

    #--------Final feature representation------
    #----1.URL presence..,2.Spam Count....,3.Words in Message body...4.Subject Length (got from EmailHeaders file)
    print('Final feature representation')
    print('1.URL presence..,2.Spam Count....,3.Words in Message body....4.Subject length')
    print(url_presence, flag_spmcount, mess_count, Header.subject_len)