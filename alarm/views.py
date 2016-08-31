from django.shortcuts import render, redirect
import datetime, unicodedata, webbrowser, time
from alarm.models import Alarm

###################################################################################
def check_alarm_time(alarm_time):
	# Consider alarm_time is a string(strftime)
	now = datetime.datetime.now().strftime("%H:%M")
	if not alarm_time >= now:
		return False
	return True

def check_and_render(request, alarm_time, s_dict, errors):
	if not check_alarm_time(alarm_time):
		error = "Please Enter a future time"
		errors.append(error)
		s_dict["errors"] = error
		return s_dict

def uni_to_str(uni):
	return unicodedata.normalize('NFKD', uni).encode('ascii','ignore')

def get_alarm_time_from_duration(duration):
	try:
		alarm_hours = int(duration[:2])
		alarm_minutes = int(duration[3:])
	except:
		alarm_hours = 0
		alarm_minutes = 0
	return (alarm_hours, alarm_minutes)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def check_and_save(request, alarm_time):
	ip = get_client_ip(request)
	current_alarm = None
	for alarm in Alarm.objects.all():
		if ip == alarm.ip_address:
			current_alarm = alarm
			break

	if current_alarm == None:
		current_alarm = Alarm(alarm_time=alarm_time, ip_address=ip)
	else:
		current_alarm.alarm_time = alarm_time

	current_alarm.save()

#####################################################################################

def alarm(request):
	"""
	Validate the input given by the user, report the errors and if no errors found  add it to the database.
	"""
	errors = []
	if "alarm_time" in request.POST and request.POST.get("alarm_time", None) != "":
		# Extract the information about the alarm_time
		alarm_time_u = request.POST.get("alarm_time", "Not Set")
		
		# Convert from unicode to python string
		alarm_time = uni_to_str(alarm_time_u)
		
		# Make datetime objects.
		try:
			alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M")
		except ValueError:
			errors.append("Please enter valid time.")
			return render(request, "index.html", {'errors' : errors})
		
		now = datetime.datetime.now()
		
		# Write it to database
		check_and_save(request, alarm_time)
		
		# Convert them from datetime objects to python strings
		now = datetime.datetime.now().strftime("%H:%M")
		alarm_time = alarm_time.strftime("%H:%M")
		
		# Preparing HTML variables.
		s_dict = {"alarm_time" : alarm_time, 'now' : now}
		s_dict = check_and_render(request, alarm_time, s_dict, errors)
		
		if not errors:
			return redirect('/success')
	
	elif "alarm_duration" in request.POST:
		# Extract the information about the alarm_time
		duration_u = request.POST.get("alarm_duration", "Not Set")
		
		# Convert from unicode to python string
		duration = uni_to_str(duration_u)
		(alarm_hours, alarm_minutes) = get_alarm_time_from_duration(duration)
		
		# Create datetime objects
		now = datetime.datetime.now()
		alarm_time = now + datetime.timedelta(hours = alarm_hours, minutes = alarm_minutes)
		
		# Save the ip and time in database
		check_and_save(request, alarm_time)	
		
		# Convert the time objects to string formats.
		now = now.strftime("%H:%M")
		alarm_time = alarm_time.strftime("%H:%M")
		
		# Prepare HTML variables.
		s_dict = {"alarm_time" : alarm_time, 'now' : now}
		s_dict = check_and_render(request, alarm_time, s_dict, errors)
		
		if not errors:
			return redirect('/success')
	
	# If no request.
	if request.POST.get("alarm_time", None) == "":
		errors.append("Please enter valid Time")
	return render(request, "index.html", {"now": datetime.datetime.now(), 'errors': errors,})

def create_alarm(request):
	ip = get_client_ip(request)
	alarm_time = datetime.datetime.now()
	for alarm in Alarm.objects.all():
		if ip == alarm.ip_address:
			alarm_time = alarm.alarm_time
			break

	alarm_time = alarm_time.strftime("%H:%M:%S")
	now = datetime.datetime.now().strftime("%H:%M")
	s_dict = {"alarm_time" : alarm_time, 'now' : now}
	return render(request, "success.html", s_dict)
