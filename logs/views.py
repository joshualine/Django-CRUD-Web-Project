from django.shortcuts import render
from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar
from . models import Topic

# Create your views here.
def index(request):
    title = "This is the calendar"
    cal = HTMLCalendar().formatmonth(2010, 1)
    return render(request, 'logs/logs_base.html', {'title':title, 'cal': cal})

def all_topics(request):
    topic_list = Topic.objects.all()
    return render(request, 'logs/topic_list.html', {'topic_list': topic_list})
