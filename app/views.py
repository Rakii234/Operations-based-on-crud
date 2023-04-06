from django.shortcuts import render
from app.models import *

# Create your views here.

def display_topic(request):
    LOT=Topic.objects.all()
    td={'topics':LOT}
    return render(request,'display_topic.html',td)

def display_webpage(request):
    WOT=Webpage.objects.all()
    wd={'webpages':WOT}
    return render(request,'display_webpage.html',wd)

def display_ac(request):
    AOT=Accessrecord.objects.all()
    ad={'access':AOT}
    return render(request,'display_ac.html',ad)