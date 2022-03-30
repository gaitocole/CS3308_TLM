#!/usr/bin/env python3

import sqlite3
import insertAlarm
import os
from datetime import date

def setUp():
	conn = sqlite3.connect("testDB.db")
	c = conn.cursor()
	c.execute("CREATE TABLE testAlarms(clientId INTEGER, theAlarm datetime);")
	conn.commit()


def tearDown():
	os.system("rm testDB.db")

def testInsertAlarm():
	conn = sqlite3.connect("testDB.db")
	c = conn.cursor()
	theAlarmDateTime = date.today()
	insertAlarm.insertAlarm("testDB.db", "testAlarms",1,theAlarmDateTime)
	try:
		c.execute("select count(clientId) from testAlarms where theAlarm = ?",  (theAlarmDateTime,))
		response = c.fetchone()[0]
		conn.commit()
		conn.close()
		if response == 1:
			print("DateTime Alarm Insert: Passed")
		else:
			print("DateTime Alarm Insert: Failed")
	except:
		print("DateTime Alarm Insert: Failed")
	


def main():
	setUp()
	testInsertAlarm()
	tearDown()

if __name__ == "__main__":
	main()


