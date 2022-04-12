#!/usr/bin/python3
import sqlite3
from datetime import datetime

def alarmSent(alarmIDNum, theDateandTime):
	conn = sqlite3.connect(alarmData.db)
	c.execute("INSERT INTO alarmHistory VALUES (?, ?);",(alarmIDNum,theDateAndTime))
	conn.commit()
	conn.close()

def createUser(phoneNumber, password, carrier):
	conn = sqlite3.connect(alarmData.db)
	c.execute("INSERT INTO userList VALUES (?, ?, ?);",(phoneNumber,password,carrier))
	conn.commit()
	conn.close()

def alterUser(oldPhoneNumber, newPhoneNumber, newPassword, newCarrier):
	conn = sqlite3.connect(alarmData.db)
	c.execute("update userlist set phoneNumber = " + newPhoneNumber + ", password = '" + newPassword + "', carrier = '" + newCarrier + "' where phoneNumber = " + oldPhoneNumber)
	conn.commit()
	conn.close()

def insertAlarm(theUserID, theTime, sunBool, monBool, tueBool, wedBool, thuBool, friBool, satBool, userMessage):
	conn = sqlite3.connect(alarmData.db)
	c.execute("INSERT INTO alarmList VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",(theUserID, theTime, sunBool, monBool, tueBool, wedBool, thuBool, friBool, satBool, userMessage))
	conn.commit()
	conn.close()

def deleteAlarm(alarmID):
	conn = sqlite3.connect(alarmData.db)
	c.execute("delete from alarmList where rowid = " + alarmID)
	conn.commit()
	conn.close()

def returnALLAlarms(theUserID):
	conn = sqlite3.connect(alarmData.db)
	c.execute("select rowID as alarmID, * from alarmList where userNumber =  " + theUserID)
	conn.commit()
	conn.close()
	return c.fetchall()

def returnAlarmsToSend(): #Still in the works
	conn = sqlite3.connect(alarmData.db)
	theDay = datetime.today().weekday()

	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	old = datetime.datetime.now() - datetime.timedelta(minutes=5)	
	if theDay == 0:
		c.execute("select rowID  as alarmID, * from alarmList where  monday = True and alarmTime > '" + old + "' and alarmTime <= '" + current_time+"'")
	conn.commit()
	conn.close()
	return c.fetchall()

 


	



