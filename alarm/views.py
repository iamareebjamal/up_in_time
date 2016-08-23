import datetime, unicodedata, webbrowser, time

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# in request's GET method : alarm_time is of the form HH:MM in the 12 hr system or
# 24 hr system depending on your input, so always use 24 hr input.

def check_alarm_time(alarm_time_u):
	now = datetime.datetime.now().strftime("%H:%M")
	alarm_time = unicodedata.normalize('NFKD', alarm_time_u).encode('ascii','ignore')
	alarm_time = alarm_time
	if not alarm_time > now:
		raise IOError
	return True

def set_alarm(alarm_time_u):
	now = datetime.datetime.now().strftime("%H:%M")
	alarm_time = unicodedata.normalize('NFKD', alarm_time_u).encode('ascii','ignore')
	while now < alarm_time:
		now = datetime.datetime.now().strftime("%H:%M")
		time.sleep(5)
	#webbrowser.open("templates/success.html") --> Do the action now

def alarm(request):
	return render(request, "alarm_base.html", {"now": datetime.datetime.now()})

def msg_set(request):
	return render(request, "alarm_set.html")

def set_alarm_with_time(request):
	"""
	I have to do this:
	Call det_alarm but I don't have to wait for it to finish and directly display the 
	message that an alarm has been set.
	"""
	alarm_time = request.GET.get("alarm_time", "Not Set")
	now = datetime.datetime.now().strftime("%H:%M")
	s_dict = {"alarm_time" : alarm_time, 'now' : now}
	try:
		check_alarm_time(alarm_time)
	except IOError:
		return render(request, "alarm_fail.html", s_dict)
	webbrowser.open("templates/alarm_set.html")
	set_alarm(alarm_time)
	return render(request, "success.html", s_dict)

def set_alarm_with_duration(request):
	duration_u = request.GET.get("alarm_duration", "Not Set")
	duration = unicodedata.normalize('NFKD', duration_u).encode('ascii','ignore')
	print(duration_u)
	try:
		alarm_hours = int(duration[:2])
		alarm_minutes = int(duration[3:])
	except:
		alarm_hours = 0
		alarm_minutes = 0
	now = datetime.datetime.now()
	alarm_time = now + datetime.timedelta(hours = alarm_hours, minutes = alarm_minutes)
	s_dict = {"alarm_time" : alarm_time, 'now' : now}
	try:
		check_alarm_time(alarm_time)
	except IOError:
		return render(request, "alarm_fail.html", s_dict)
	webbrowser.open("templates/alarm_set.html")
	set_alarm(alarm_time)
	s_dict = {"alarm_time":alarm_time}
	return render(request, "success.html", s_dict)
