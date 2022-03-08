import sqlite3
import primary_notification2 as pn
import unittest

class notificationSettingTest(unittest.TestCase):

    def test_Notification(self):

        dbname1 = "C:/Users/ASueppel/iCloudDrive/Spring 2022/CSPB 3308/Project/notification.db"
        username1 = 'asueppel1990'
        notification1 = 'text'
        userinfo1 = [(username1, notification1)]

        conn = sqlite3.connect('C:/Users/ASueppel/iCloudDrive/Spring 2022/CSPB 3308/Project/notification.db')
        c = conn.cursor()

        pn.create(dbname1)
        pn.primaryNotification2(dbname1, userinfo1)

        for row in c.execute('SELECT * FROM Notification'):
            user = row[0]
            notification = row[1]

        self.assertEqual(user, 'asueppel1990', 'Passed')
        self.assertEqual(notification, 'text', 'Passed')

if __name__ == '__main__':
    unittest.main()