from django.shortcuts import render
import datetime, unicodedata, webbrowser, time

###################################################################################
def check_alarm_time(alarm_time):
	# Consider alarm_time is a string(strftime)
	now = datetime.datetime.now().strftime("%H:%M")
	if not alarm_time > now:
		return False
	return True

def check_and_render(request, alarm_time, s_dict):
	if not check_alarm_time(alarm_time):
		error = True
		s_dict["error"] = error
		return render(request, "index.html", s_dict)

def uni_to_str(uni):
	return unicodedata.normalize('NFKD', uni).encode('ascii','ignore')

def set_alarm(alarm_time):
	# Consider alarm_time is a string(strftime)
	now = datetime.datetime.now().strftime("%H:%M")
	#alarm_time = unicodedata.normalize('NFKD', alarm_time_u).encode('ascii','ignore')
	
	# It blocks the loading period so that page loads only after alarm time
	while now < alarm_time:
		now = datetime.datetime.now().strftime("%H:%M")
		time.sleep(5)

def get_alarm_time(duration):
	try:
		alarm_hours = int(duration[:2])
		alarm_minutes = int(duration[3:])
	except:
		alarm_hours = 0
		alarm_minutes = 0
	return (alarm_hours, alarm_minutes)

#####################################################################################

def alarm(request):
	errors =[]
	if "alarm_time" in request.GET:
		alarm_time_u = request.GET.get("alarm_time", "Not Set")
		alarm_time = uni_to_str(alarm_time_u)
		now = datetime.datetime.now().strftime("%H:%M")
		s_dict = {"alarm_time" : alarm_time, 'now' : now}
		check_and_render(request, alarm_time, s_dict)
		webbrowser.open("templates/alarm_set.html")
		set_alarm(alarm_time)
		return render(request, "success.html", s_dict)
	
	elif "alarm_duration" in request.GET:
		duration_u = request.GET.get("alarm_duration", "Not Set")
		duration = uni_to_str(duration_u)
		(alarm_hours, alarm_minutes) = get_alarm_time(duration)
		now = datetime.datetime.now()
		alarm_time = now + datetime.timedelta(hours = alarm_hours, minutes = alarm_minutes)
		now = now.strftime("%H:%M")
		alarm_time = alarm_time.strftime("%H:%M")
		s_dict = {"alarm_time" : alarm_time, 'now' : now}
		check_and_render(request, alarm_time, s_dict)
		webbrowser.open("templates/alarm_set.html")
		set_alarm(alarm_time)
		return render(request, "success.html", s_dict)
	
	# If no request.
	return render(request, "index.html", {"now": datetime.datetime.now(), 'errors': errors,})
	