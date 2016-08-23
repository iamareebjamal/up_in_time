from django.shortcuts import render
import datetime, unicodedata, webbrowser, time

def check_alarm_time(alarm_time):
	# Consider alarm_time is a string(strftime)
	now = datetime.datetime.now().strftime("%H:%M")
	if not alarm_time > now:
		raise IOError
	return True

def set_alarm(alarm_time):
	# Consider alarm_time is a string(strftime)
	now = datetime.datetime.now().strftime("%H:%M")
	#alarm_time = unicodedata.normalize('NFKD', alarm_time_u).encode('ascii','ignore')
	
	# It blocks the loading period so that page loads only after alarm time
	while now < alarm_time:
		now = datetime.datetime.now().strftime("%H:%M")
		time.sleep(5)
	
def alarm(request):
	return render(request, "index.html", {"now": datetime.datetime.now()})

def msg_set(request):
	return render(request, "alarm_set.html")

def set_alarm_with_time(request):
	"""
	I have to do this:
	Call det_alarm but I don't have to wait for it to finish and directly display the 
	message that an alarm has been set.
	"""
	alarm_time_u = request.GET.get("alarm_time", "Not Set")
	alarm_time = unicodedata.normalize('NFKD', alarm_time_u).encode('ascii','ignore')
	now = datetime.datetime.now().strftime("%H:%M")
	s_dict = {"alarm_time" : alarm_time, 'now' : now}
	try:
		check_alarm_time(alarm_time)
	except IOError:
		s_dict["error"] = True
		return render(request, "index.html", s_dict)
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
		check_alarm_time(alarm_time.strftime("%H:%M"))
	except IOError:
		s_dict["error"] = True
		return render(request, "index.html", s_dict)
	webbrowser.open("templates/alarm_set.html")
	set_alarm(alarm_time.strftime("%H:%M"))
	s_dict = {"alarm_time":alarm_time}
	return render(request, "success.html", s_dict)
