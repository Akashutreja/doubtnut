from .models import UserProfile
import datetime

def my_cron_job():
  active_on = datetime.datetime.now()
  next_five_minute = active_on - datetime.timedelta(minute = 5)
  print(active_on, next_five_minute)
  queryset = UserProfile.filter(last_activity__range=(active_on, next_five_minute) )
  print(queryset.count)