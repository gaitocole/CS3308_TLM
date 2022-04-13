#!/usr/bin/python3

#tmobile @tmomail.net
#ATT 	 @txt.att.net
#Verizon @vtext.com

#For use for CU CS3308 Student project
import smtplib
import emailconfig

def send_email(subject, msg):
	try:
		#creating a SMTP session
		s = smtplib.SMTP('smtp.gmail.com:587')
		
		s.ehlo()

		#start TLS for security
		s.starttls()

		#Authentication
		#s.login(emailconfig.Email_Address, emailconfig.Password)
		s.login("cs3308tasklist@gmail.com", "CUSchoolProject")

		#Message to be sent
		message = 'Subject: {}\n\n{}'.format(subject, msg)		

		#send the email sender/receiver
		s.sendmail("cs3308tasklist@gmail.com", "cs3308tasklist@gmail.com", message)

		#end session
		s.quit()
		print("Success Email sent")

	except:
		print("Email failed to send.")


subject = "Test subject"
msg = "Hello this is a test of the email system!"

send_email(subject, msg)
