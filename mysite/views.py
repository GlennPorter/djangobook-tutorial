from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse('Hello world')

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', { 'current_date': now })

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dateTime = datetime.datetime.now() + datetime.timedelta(hours = offset)
	return render(request, 'hours_ahead.html', { 'hour_offset': offset, 'next_time': dateTime })

def search_form(request):
	return render(request, 'search_form.html')