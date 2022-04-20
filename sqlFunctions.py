#!/usr/bin/python3
import sqlite3
from datetime import datetime, timedelta

def alarmSent(alarmIDNum, theDateandTime):
	conn = sqlite3.connect('alarmData.db')
	conn.execute("INSERT INTO alarmHistory VALUES (?, ?);",(alarmIDNum,theDateAndTime))
	conn.commit()
	conn.close()

def createUser(phoneNumber, password, carrier):
	conn = sqlite3.connect('alarmData.db')
	conn.execute("INSERT INTO userList VALUES (?, ?, ?);",(phoneNumber,password,carrier))
	conn.commit()
	conn.close()

def alterUser(oldPhoneNumber, newPhoneNumber, newPassword, newCarrier):
	conn = sqlite3.connect('alarmData.db')
	conn.execute("update userlist set phoneNumber = " + str(newPhoneNumber) + ", password = '" + newPassword + "', carrier = '" + newCarrier + "' where phoneNumber = " + str(oldPhoneNumber))
	conn.commit()
	conn.close()

def insertAlarm(theUserID, theTime, sunBool, monBool, tueBool, wedBool, thuBool, friBool, satBool, userMessage):
	conn = sqlite3.connect('alarmData.db')
	conn.execute("INSERT INTO alarmList VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",(theUserID, theTime, sunBool, monBool, tueBool, wedBool, thuBool, friBool, satBool, userMessage))
	conn.commit()
	conn.close()

def deleteAlarm(alarmID):
	conn = sqlite3.connect('alarmData.db')
	conn.execute("delete from alarmList where rowid = " + str(alarmID))
	conn.commit()
	conn.close()

def returnALLAlarms(theUserID):
	conn = sqlite3.connect('alarmData.db')
	cursor = conn.cursor()
	cursor.execute("select rowID as alarmID, * from alarmList where userNumber =  " + str(theUserID))
	return cursor.fetchall()

def returnAlarmsToSend(): #Still in the works
	conn = sqlite3.connect('alarmData.db')
	theDay = datetime.today().isoweekday()
	cursor = conn.cursor()
	now = (datetime.now()).strftime('%H:%M:%S')
	#current_time = now
	old = (datetime.now() - timedelta(minutes=5)).strftime('%H:%M:%S')
	if theDay == 2:
		cursor.execute("select userNumber, alarmTime, userMessage, userList.phoneNumber, userList.carrier from alarmList join userList on userNumber =  userList.rowID where sunday = 1 and alarmTime > '" + old + "' and alarmTime <= '" + now +"'")
	return cursor.fetchall()

def getUserID(userPhoneNumber):
	conn = sqlite3.connect('alarmData.db')
	cursor = conn.cursor()
	cursor.execute("select rowID as userID from userList where phoneNumber =  " + str(userPhoneNumber))
	return cursor.fetchone()[0]

def getUserInfo():
	conn = sqlite3.connect('alarmData.db')
	cursor = conn.cursor()
	cursor.execute("select rowID, * from userList " )
	return cursor.fetchall()

	


def main():
	#alterUser(8179992239,8179992230, 'Jako', 'ATTs')
	#print(getUserID(8179992230))
	#insertAlarm(1,'20:49:00',1,0,1,0,0,0,0,"Call your wife")
	#print(returnALLAlarms(1))
	#print(returnAlarmsToSend())
	print(getUserInfo())
	#deleteAlarm(1)

if __name__ == "__main__":
	main()