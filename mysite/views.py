from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render

import datetime

def hello(request):
	return HttpResponse("Hello World!")

def current_datetime(request):
	now = datetime.datetime.now()
	s_dict = {'current_datetime' : now}
	return render(request, 'current_datetime.html', s_dict)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	now = datetime.datetime.now() 
	dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
	s_dict = {'now' : now, 'dt': dt, 'offset' : offset}
	return render(request, 'hours_ahead.html', s_dict)
	