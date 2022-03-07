import sqlite3

dbname1 = "C:/Users/ASueppel/iCloudDrive/Spring 2022/CSPB 3308/Project/notification.db"

def create(dbname):

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS Notification (user VARCHAR PRIMARY KEY, notification CHAR);")

    conn.commit()
    conn.close()

def primaryNotification2(dbname, userinfo):

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    for i in userinfo:
        c.execute("INSERT INTO Notification VALUES (?, ?)", i)

    conn.commit()
    conn.close()

username1 = input("Please enter username: ")
notification1 = input("Please enter notification preference: ")
userinfo1 = [(username1, notification1)]

create(dbname1)
primaryNotification2(dbname1, userinfo1)