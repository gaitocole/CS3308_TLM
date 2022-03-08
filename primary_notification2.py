import sqlite3

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