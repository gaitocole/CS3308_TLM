#usr/bin/python3
#For use for CU CS3308 Student project
import smtplib

#creating a SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

#start TLS for security
s.starttls()

#Authentication
s.login("cs3308tasklist@gmail.com", "CUSchoolProject")

#Message to be sent
message = "Message to be sent"

#send the email sender/receiver
s.sendmail("cs3308tasklist@gmail.com", "coga6899@colorado.edu")

#end session
s.quit

#Print Confirmation of email sent
print('Mail Sent')
