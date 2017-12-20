#############################################################
#                       WhoSpammin?                         #
#       RIT CSEC 462 - Network Security Project 2017        #
# Written by: Michael Schade, Ben Goldfarb, Brendon Anderson#
#############################################################

import imaplib
import email
import re
import getpass

from collections import Counter

import itertools

emailAddr = input("Enter your gmail address: ")
passwd = getpass.getpass("Enter your password: ")
server = "imap.gmail.com"
port  = 993
emailEnd = emailAddr + "@gmail.com"

#print(emailEnd)


mail = imaplib.IMAP4_SSL(server)
mail.login(emailAddr, passwd)

mail.select('[Gmail]/Spam')

#mailboxes = mail.list()




temp, data = mail.search(None, "ALL")
#print(data)

lst = []

for x in data[0].split():
    temp, msg_data = mail.fetch(x, '(RFC822)')
    for response in msg_data:
        if isinstance(response, tuple):
            part = response[1].decode('utf-8')
            msg = email.message_from_string(part)
            #print(msg)
            sendIP = msg['Received-SPF']
            #print(sendIP)
            email2 = re.findall('[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+', sendIP)
            #print(email2)
            ipAddr = re.findall('(?<==).*(?=;$)', sendIP)

            element = email2 + ipAddr
            lst.append(element)






with open('mail.csv', 'w') as f:
    f.write("id,value\n")
    for k, g in itertools.groupby(lst):
        temp = k, sum(1 for _ in g)
        temp2 = str(temp)
        temp2 = temp2.replace("'", "")
        temp2 = temp2.replace("[", "")
        temp2 = temp2.replace("]", "")
        temp2 = temp2.replace("(", "")
        temp2 = temp2.replace(")", "")
        temp2 = temp2.replace(",", ":", 1)
        temp2 = temp2.replace(" ", "", 1)
        #print(temp2)
        f.write(temp2 + "\n")
print('Output for '+ emailEnd + ' written to mail.csv')
