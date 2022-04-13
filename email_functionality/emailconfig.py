#!/usr/bin/python3

#Email domains
#tmobile @tmomail.net
#ATT 	 @txt.att.net
#Verizon @vtext.com

import send_email

subject = "Test subject"
msg = "Hello this is a test of the email system!"
list_of_emails = ['gaitocole@gmail.com', 'cs3308tasklist@gmail.com', '3032415637@vtext.com']

for email in list_of_emails:
	send_email.send_email(email, subject, msg)