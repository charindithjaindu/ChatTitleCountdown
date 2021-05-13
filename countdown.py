import time
import datetime
from pyrogram import Client
import os


cnl=os.getenv("GROUP_ID")
session=os.getenv("SESSION")
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
date_of_end=os.getenv("DATE")

paras=date_of_end.split(' ')

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

def countdown(stop):
    while True:
        difference = stop - datetime.datetime.now()
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)
        if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            print("Good bye!")
            break
        count_months=diff_month(stop,datetime.datetime.now())
        count_weeks=int(difference.days/7)
        final_str=(str(count_months) + " months | "
        	  + str(count_weeks) + " weeks | "
              + str(difference.days) + " days | "
              +str(difference.days*24)+" hours | "
              +str(difference.days*24*60)+" mins"
              )
        return final_str

for i in range(len(paras)):
	paras[i]=int(paras[i])
	
exam_date = datetime.datetime(int(paras[0]), int(paras[1]), int(paras[2]), int(paras[3]), int(paras[4]), int(paras[5]))

print(countdown(exam_date))

with Client(session, api_id, api_hash) as app:
	while True:
	    app.set_chat_title(cnl,countdown(exam_date))
	    print('changes')
	    time.sleep(60)
