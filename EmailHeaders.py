import numpy
import csv
import re
import email.utils
#from EmailGo import emailAnalyzer
import RabinKarp
from email.parser import HeaderParser
from mailbox import mbox
from validate_email import validate_email

class Header:
    valid_from_email = 0
    valid_sender_email = 0
    valid_reply_email = 0
    valid_to_email = 0
    valid_cc_email = 0
    valid_bcc_email = 0
    subject_len = 0

    domain_name = ''
    frm_domain = ''

    returEC = [0]
    k = 0
    l = 0
    valueEC = 0  #Valid of the Email Client Software

    is_valid_addr = [] * 2
    is_valid_addr_to = [] * 2
    flag_recvd = 0

    message_id = 0

    f = open("D:\\Srihari\\Spam filtering\\20021010_spam.tar\\0018.259154a52bc55dcae491cfded60a5cd2",'r')
    #0010.7f5fb525755c45eb78efc18d7c9ea5aa
    flag = 1
    #print('f', f)

    for line in f:
        #print(line)

        #----BLOCK START---------
        #Retrieving and checking From email Address of Sender

        chk_ln_fromaddr = re.search(r'From:', line, re.M)
        if chk_ln_fromaddr:
            print("flag", flag)
            print("line", line)
            from_add = line.split(':', 1)
            from_addr = from_add[1]
            print('From Add', from_addr)
            sendr_strindx = from_addr.find('<')
            print('starting index', sendr_strindx)
            sendr_endindx = from_addr.find('>')
            print('ending index', sendr_endindx)
            from_email = from_addr[sendr_strindx+1:sendr_endindx]
            print('Sender Email Address', from_email)
            is_valid_addr = validate_email(from_email)
            print('Validating the Email Address', is_valid_addr)
            if is_valid_addr:
                valid_from_email = 1
                print('Validity of from address of email', valid_from_email)
            else:
                valid_from_email = 0
                print('Validity of from address of email', valid_from_email)
            #To check whether it has valid SMTP server
            is_valid_addr = validate_email(from_email, check_mx= True)
            print('Validating if the host has SMTP Server', is_valid_addr)
            is_valid_addr = validate_email(from_email, verify=True)
            print('Verifying whether the email exists', is_valid_addr)

        else:
            print("From Address not present")
         #------BLOCK END--------------
        flag = flag + 1

        # ----BLOCK START---------
        # Retrieving and checking Sender email Address of Sender

        chk_ln_senderaddr = re.search(r'Sender:', line, re.M | re.I)
        if chk_ln_senderaddr:
            #print("flag", flag)
            print("line", line)
            sendr_add = line.split(':', 1)
            sendr_addr = sendr_add[1]
            print('Sender Add', sendr_addr)
            sendr_strindx = sendr_addr.find('<')
            print('starting index', sendr_strindx)
            sendr_endindx = sendr_addr.find('>')
            print('ending index', sendr_endindx)
            sendr_email = sendr_addr[sendr_strindx + 1:sendr_endindx]
            print('Sender Email Address', sendr_email)
            # is_valid_addr = validate_email(from_email)
            is_valid_addr = validate_email(sendr_email)
            print('Validating the Email Address', is_valid_addr)
            if is_valid_addr:
                valid_sender_email = 1
                print('Validity of sender address of email', valid_sender_email)
            else:
                valid_sender_email = 0
                print('Validity of sender address of email', valid_sender_email)
            # To check whether it has valid SMTP server
            is_valid_addr = validate_email(sendr_email, check_mx=True)
            print('Validating if the host has SMTP Server', is_valid_addr)
            is_valid_addr = validate_email(sendr_email, verify=True)
            print('Verifying whether the email exists', is_valid_addr)

        else:
            print("Sender Address not present")
            # ------BLOCK END--------------

        # ----BLOCK START---------
        # Retrieving and checking reply-To email Address of Sender

        chk_ln_replytoaddr = re.search(r'Reply-To:', line, re.M | re.I)
        if chk_ln_replytoaddr:
            # print("flag", flag)
            print("line", line)
            replyto_add = line.split(':', 1)
            replyto_addr = replyto_add[1]
            print('Replyto Add', replyto_addr)
            sendr_strindx = replyto_addr.find('<')
            print('starting index', sendr_strindx)
            sendr_endindx = replyto_addr.find('>')
            print('ending index', sendr_endindx)
            replyto_email = replyto_addr[sendr_strindx + 1:sendr_endindx]
            print('ReplyTo Email Address', replyto_email)
            # is_valid_addr = validate_email(from_email)
            is_valid_addr = validate_email(replyto_email)
            print('Validating the Email Address', is_valid_addr)
            if is_valid_addr:
                valid_reply_email = 1
                print('Validity of Reply-To address of email', valid_reply_email)
            else:
                valid_reply_email = 0
                print('Validity of Reply-To address of email', valid_reply_email)
            # To check whether it has valid SMTP server
            is_valid_addr = validate_email(replyto_email, check_mx=True)
            print('Validating if the host has SMTP Server', is_valid_addr)
            is_valid_addr = validate_email(replyto_email, verify=True)
            print('Verifying whether the email exists', is_valid_addr)

        else:
            print("ReplyTo Address not present")
            # ------BLOCK END--------------

        # ----BLOCK START---------
        # Retrieving and checking To email Address of Sender
        chk_ln_toaddr = re.search(r'To:', line)
        if chk_ln_toaddr:
            # print("flag", flag)
            print("line", line)
            to_add = line.split(':', 1)
            to_addr = to_add[1]
            print('To Add', to_addr)
            sendr_strindx = to_addr.find('<')
            print('starting index', sendr_strindx)
            sendr_endindx = to_addr.find('>')
            print('ending index', sendr_endindx)
            coma_indx = to_addr.find(',')
            if (sendr_strindx & sendr_endindx == -1) & (coma_indx != -1):
                print('coma', coma_indx)
                to_addr_ls = to_addr.split(',')
                to_addr_ls.pop()
                #to_addr_ls = to_addr_ls[-1]
                print('check before', to_addr_ls)
                #lis = 0
                #print('1st To address', to_addr_ls[0])
                #print('2nd To address', to_addr_ls[1])
                for add_ls in to_addr_ls:
                    print('chk_lis', add_ls)
                    is_valid_addr = validate_email(add_ls)
                    print('Validating the Email Address', is_valid_addr)
                    if is_valid_addr:
                        valid_to_email = 1
                        print('Validity of To address of email', valid_to_email)
                    else:
                        valid_to_email = 0
                        print('Validity of To address of email', valid_to_email)
                    # To check whether it has valid SMTP server
                    is_valid_addr = validate_email(add_ls, check_mx=True)
                    print('Validating if the host has SMTP Server', is_valid_addr)
                    is_valid_addr = validate_email(add_ls, verify=True)
                    print('Verifying whether the email exists', is_valid_addr)
                    #lis = lis+1
            elif (sendr_strindx & sendr_endindx != -1) & (coma_indx == -1):
                to_email = to_addr[sendr_strindx + 1:sendr_endindx]
                print('To Email Address', to_email)
                # is_valid_addr = validate_email(from_email)
                is_valid_addr = validate_email(to_email)
                print('Validating the Email Address', is_valid_addr)
                if is_valid_addr:
                    valid_to_email = 1
                    print('Validity of To address of email', valid_to_email)
                else:
                   valid_to_email = 0
                   print('Validity of To address of email', valid_to_email)
                # To check whether it has valid SMTP server
                is_valid_addr = validate_email(to_email, check_mx=True)
                print('Validating if the host has SMTP Server', is_valid_addr)
                is_valid_addr = validate_email(to_email, verify=True)
                print('Verifying whether the email exists', is_valid_addr)
            else:
                is_valid_addr = validate_email(to_addr)
                print('Validating the Email Address', is_valid_addr)
                if is_valid_addr:
                    valid_to_email = 1
                    print('Validity of To address of email', valid_to_email)
                else:
                    valid_to_email = 0
                    print('Validity of To address of email', valid_to_email)
                # To check whether it has valid SMTP server
                is_valid_addr = validate_email(to_addr, check_mx=True)
                print('Validating if the host has SMTP Server', is_valid_addr)
                is_valid_addr = validate_email(to_addr, verify=True)
                print('Verifying whether the email exists', is_valid_addr)
        else:
            print("To Address not present")
            # ------BLOCK END--------------

            # ----BLOCK START---------
            # Retrieving and checking CC email Address of Sender
        chk_ln_ccaddr = re.search(r'Cc:', line)
        if chk_ln_ccaddr:
            # print("flag", flag)
            print("line", line)
            cc_add = line.split(':', 1)
            cc_addr = cc_add[1]
            print('CC Add', cc_addr)
            sendr_strindx = cc_addr.find('<')
            print('starting index', sendr_strindx)
            sendr_endindx = cc_addr.find('>')
            print('ending index', sendr_endindx)
            cc_email = cc_addr[sendr_strindx + 1:sendr_endindx]
            print('Cc Email Address', cc_email)
            # is_valid_addr = validate_email(from_email)
            is_valid_addr = validate_email(cc_email)
            print('Validating the Email Address', is_valid_addr)
            if is_valid_addr:
                valid_cc_email = 1
                print('Validity of Cc address of email', valid_cc_email)
            else:
                valid_cc_email = 0
                print('Validity of Cc address of email', valid_cc_email)
            # To check whether it has valid SMTP server
            is_valid_addr = validate_email(cc_email, check_mx=True)
            print('Validating if the host has SMTP Server', is_valid_addr)
            is_valid_addr = validate_email(cc_email, verify=True)
            print('Verifying whether the email exists', is_valid_addr)

        else:
            print("Cc Address not present")
            # ------BLOCK END--------------

            # ----BLOCK START---------
            # Retrieving and checking BCC email Address of Sender
        chk_ln_bccaddr = re.search(r'BCC:', line)
        if chk_ln_bccaddr:
            # print("flag", flag)
            print("line", line)
            bcc_add = line.split(':', 1)
            bcc_addr = bcc_add[1]
            print('BCC Add', bcc_addr)
            sendr_strindx = bcc_addr.find('<')
            print('starting index', sendr_strindx)
            sendr_endindx = bcc_addr.find('>')
            print('ending index', sendr_endindx)
            bcc_email = bcc_addr[sendr_strindx + 1:sendr_endindx]
            print('BCC Email Address', bcc_email)
            # is_valid_addr = validate_email(from_email)
            is_valid_addr = validate_email(bcc_email)
            print('Validating the Email Address', is_valid_addr)
            if is_valid_addr:
                valid_bcc_email = 1
                print('Validity of BCC address of email', valid_bcc_email)
            else:
                valid_bcc_email = 0
                print('Validity of BCC address of email', valid_bcc_email)
            # To check whether it has valid SMTP server
            is_valid_addr = validate_email(bcc_email, check_mx=True)
            print('Validating if the host has SMTP Server', is_valid_addr)
            is_valid_addr = validate_email(bcc_email, verify=True)
            print('Verifying whether the email exists', is_valid_addr)

        else:
            print("BCC Address not present")
                # ------BLOCK END--------------

        #------BLOCK START---------------------------
        #------Manipulating and validating the Received block
        chk_ln_receivedblk = re.search(r'Received:', line, re.M|re.I)
        if chk_ln_receivedblk:
            flag_recvd = flag_recvd + 1

        # --X-Mailer ID-------------------------------
        chk_In_XMailer = re.search(r'X-Mailer:', line, re.M|re.I)
        if chk_In_XMailer:
            print('X-Mailer present',line)
            colon_indx_str = line.find(':')
            #Regular Expression is used to search for first integer in a string
            colon_indx_end_no = re.search('\d', line)
            colon_indx_end_brkt = re.search(r'[(]',line)
            if (colon_indx_end_no or colon_indx_end_brkt):
                #print('index_integer_number', colon_indx_end_no.start())
                #print('index_integer_bracket', colon_indx_end_brkt.start())
                #if colon_indx_end_no:
                #   xmailer_nam = line[colon_indx_str + 1:colon_indx_end_no.start()]
                #elif colon_indx_end_brkt:
                #    xmailer_nam = line[colon_indx_str + 1:colon_indx_end_brkt.start()-2]
                xmailer_nam = line[colon_indx_str + 1:]
                print('X-mailer', xmailer_nam)
                q = 101
                clientSoftware = ['Alpine', '@Mail', 'Balsa', 'Becky! Internet Mail', 'BlitzMail', 'Citadel, Claws Mail',
                                  'Cone', 'Courier', 'Elm', 'eM Client', 'EmailTray', 'Eudora OSE', 'Eureka Email', 'Evolution', 'FirstClass',
                                  'Forte Agent', 'Geary', 'GNUMail', 'Gnus', 'GroupWise', 'IBM Notes', 'IMP', 'Inky',
                                  'KMail', 'Libremail', 'Mailbird', 'Mailpile', 'mailx', 'Microsoft Entourage', 'Microsoft Outlook',
                                  'Mozilla Mail & Newsgroups', 'nmh', 'MH', 'Mozilla Thunderbird', 'Mulberry', 'Mutt', 'Netscape Messenger',
                                  'Opera Mail', 'Outlook Express','Pegasus Mail', 'Pine', 'Pocomail', 'Ream', 'RoundCube', 'SeaMonkey Mail & Newsgroups',
                                  'Spicebird', 'SquirrelMail', 'Sylpheed', 'The Bat!', 'Turnpike', 'Windows Live Mail',
                                  'Windows Mail', 'WorldClient', 'XgenPlus', 'YAM', 'Zimbra']

                for k, cs in enumerate(clientSoftware):
                    #print('cs', cs)
                    #print('k', k)
                    retEC = RabinKarp.rbk(xmailer_nam, clientSoftware[k], q)
                    returEC.append(retEC)
                    print('retu', retEC)

                for l in returEC:
                    if l == 1:
                        valueEC = 1
                        break
                    print('EC presence', l)
                #print('EC presence', list(range(retEC)))
                print('1 - Presence & 0 - Absence of Client Software', valueEC)
                print('End of for loop')

        #Message-ID
        #Take the domain name from Message-ID field and From field
        chk_ln_Messageid = re.search(r'Message-Id:', line, re.M | re.I)
        if chk_ln_Messageid:
            print('Message-ID', line)
            mid_stridx = line.find('@')
            mid_endidx = line.find('>')
            dom_name = line[mid_stridx+1: mid_endidx]
            print('Domain Name from Message-ID', dom_name)
            domain_name = dom_name
            print('chk1', domain_name)

        chk_ln_fromaddr2 = re.search(r'From:', line, re.M | re.I)
        if chk_ln_fromaddr2:
            print('From address', line)
            frm_stridx = line.find('@')
            frm_dom_name = line[frm_stridx:]
            print('Domain Name from From address', frm_dom_name)
            frm_domain = frm_dom_name
            print('chk2', frm_domain)

        if (domain_name == frm_domain):
            message_id = 1
            print('Domain Name Matching and hence Ham mail')
        else:
            message_id = 0
            print('Domain Name Not Matching and hence Spam mail')

        chk_In_subject = re.search(r'Subject:', line, re.M)
        if chk_In_subject:
            print('Subject', line)
            sub_idx = line.find(':')
            sub_stng = line[sub_idx+2:]
            print('subject content', sub_stng)
            sub_stng = " ".join(sub_stng.split())
            subject_len = len(sub_stng)
            print('subject trimmed', sub_stng)
            print('subject length', subject_len)

    recvd_count = flag_recvd

    print ('Validity values')
    print (valid_from_email, valid_sender_email, valid_reply_email, valid_to_email, valid_cc_email, valid_bcc_email, recvd_count, valueEC, message_id)