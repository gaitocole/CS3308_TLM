#!/usr/bin/python3
import sqlite3

#Take a database, a client number (this should just be an int referencing a cell num), and a datetime into an insert table
def insertAlarm(dbname, tblName, client, alarm):
	conn = sqlite3.connect(dbname)
	c = conn.cursor()
	c.execute("INSERT INTO " + tblName + " VALUES (?, ?);", (int(client),alarm))
	conn.commit()
	conn.close()
