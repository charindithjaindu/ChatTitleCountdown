import time
import datetime
from pyrogram import Client
import os


cnl=os.getenv("GROUP_ID")
session=os.getenv("SESSION")
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")


def countdown(stop):
    while True:
        difference = stop - datetime.datetime.now()
        count_weeks=int(difference.days/7)
        final_str=(str(int(difference.days/30)) + " months | "
              + str(count_weeks) + " weeks | "
              + str(difference.days) + " days | "
              +str(int(difference.days*24+difference.seconds/3600))+" hours | "
              +str(int(difference.days*24*60+difference.seconds/60))+" mins"
              )
        return final_str

exam_date = datetime.datetime(2021, 10 ,4 ,7, 0 ,0)

print(countdown(exam_date))

with Client(session, api_id, api_hash) as app:
	while True:
	    app.set_chat_title(cnl,countdown(exam_date))
	    print('changes')
	    time.sleep(86400)
