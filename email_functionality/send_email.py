#!/usr/bin/python3

#For use for CU CS3308 Student project
import smtplib

def send_email(receiver, subject, msg):
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
		#s.sendmail("cs3308tasklist@gmail.com", "cs3308tasklist@gmail.com", message)
		s.sendmail("cs3308tasklist@gmail.com", receiver, message)

		#end session
		s.quit()
		print("Success Email sent")

	except:
		print("Email failed to send.")