import sqlite3
# import primary_notification
# import os

conn = sqlite3.connect('C:/Users/ASueppel/iCloudDrive/Spring 2022/CSPB 3308/Project/notification.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM Notification'):
    user = row[0]
    notification = row[1]
    print(user, notification)

assert user == 'asueppel1990'
assert notification == 'email'
