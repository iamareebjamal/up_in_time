import datetime, unicodedata

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def alarm(request):
	return render(request, "alarm_base.html")

def set_alarm_with_time(request):
	alarm_time = request.GET.get("alarm_time", "Not Set")
	now = datetime.datetime.now()
	s_dict = {"alarm_time" : alarm_time, 'now' : now}
	try:
		set_alarm(alarm_time)
		return render(request, "alarm_set.html", s_dict)
	except:
		return render(request, "alarm_fail.html", s_dict)

def set_alarm(alarm_time):
	return None	

def set_alarm_with_duration(request):
	duration_u = request.GET.get("alarm_duration", "Not Set")
	duration = unicodedata.normalize('NFKD', duration_u).encode('ascii','ignore')
	try:
		alarm_hours = int(duration[:2])
		alarm_minutes = int(duration[3:])
	except:
		alarm_hours = 0
		alarm_minutes = 0
	now = datetime.datetime.now()
	alarm_time = now + datetime.timedelta(hours = alarm_hours, minutes = alarm_minutes)
	s_dict = {"alarm_time" : alarm_time, 'now' : now}
	return render(request, "alarm_set.html", s_dict)