from email.header import Header
from email.message import Message

#msg = Message()
#msg['Subject'] =
#print (msg.as_st

import email
import poplib
import string, random
import io
import logging

SERVER = "pop.gmail.com"

##ENTER USERNAME AND PASSWORD###
USER = ""
PASSWORD = ""

# connect to server
logging.debug('connecting to ' + SERVER)
server = poplib.POP3_SSL(SERVER)
# server = poplib.POP3(SERVER)

# log in
logging.debug('log in')
server.user(USER)
server.pass_(PASSWORD)

# list items on server
logging.debug('listing emails')
resp, items, octets = server.list()

#HEADER
# download the first message in the list
id, size = string.split(items[0])
resp, text, octets = server.retr(id)

# convert list to Message object
text = string.join(text, "\n")


print(text)


id, size = string.split(items[1])
resp, text, octets = server.retr(id)

text2 = string.join(text,"\n")
print(text2)







#print(text2.count("Subject: "))

#file = io.StringIO(text)
#message = Message(text)

# output message
#print(message['From']),
#print(message['Subject']),
#print(message['Date']),
# print(message.fp.read())




###IMAP#####

import imaplib

obj = imaplib.IMAP4_SSL('imap.gmail.com', 993)
obj.login(USER, PASSWORD)
obj.select('INBOX')

#obj.search(None, 'UnSeen')


#How many unread messages
status, response = obj.status('INBOX', "(UNSEEN)")
unread = int(response[0].split()[2].strip(').,]'))
print(unread)


###From who###
#status, response = obj.search(None, '(FROM "%s")' % name)
