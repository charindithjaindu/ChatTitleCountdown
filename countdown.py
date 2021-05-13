import time
import datetime
from pyrogram import Client


cnl=-1001122759576

session='BQDCm62kIyYO9W3IPmOzQGm_1PIw55BhlMYDt6dBmXUFjUk568t1l5GRSYPmCUD6GqIHqM98d9B-uqSVRgIqOjpFY_uIAUN2PsO-LzDIHi4r2IXTyfj49MXsTuqTvE6_a86c222g_Ok8-1PvJe9WOSz096gyoO38Q3KrZTENdSRPHP1leifS_NscHK6uo0vx5q-lJPbX8JkB-geGG_cINdagS3cRKdafop4bn9E7vC9yNegLhegMXI7pDxO_sfnnhnKGkXEHYaxm2_T8VuoP6chnOGewFUTPSOPakdogZbfb-Vnh5fq0yMq3SMNkbvLlVhLjDl0bIfjPUVXePSSdC0kuQsDMBAA'
api_id = 3214909
api_hash = '79432f0d96d7ba443b07a0b5a36fdcf9'


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



exam_date = datetime.datetime(2021, 10, 4, 7, 0, 0)

print(countdown(exam_date))

with Client(session, api_id, api_hash) as app:
	while True:
	    app.set_chat_title(cnl,countdown(exam_date))
	    print('changes')
	    time.sleep(60)