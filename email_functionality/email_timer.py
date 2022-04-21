#the purpose of this function is to verify every five minutes if there is
#another alarm series which need to be sent out

#Author Cole Gaito

import sched, time
#import /sqlFunctions.py

s = sched.scheduler(time.time, time.sleep)
def alarm_check(sc):
	a = time.time
	print("Sending Emails at a")
	sc.enter(300, 1, alarm_check, (sc,))

s.enter(300, 1, alarm_check, (s,))
s.run()

