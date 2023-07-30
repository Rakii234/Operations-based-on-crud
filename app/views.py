from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.

def display_topic(request):
    LOT=Topic.objects.all()
    td={'topics':LOT}
    return render(request,'display_topic.html',td)

def display_webpage(request):
    WOT=Webpage.objects.all()
    WOT=Webpage.objects.filter(topic_name='Cricket')
    WOT=Webpage.objects.exclude(topic_name='Cricket')
    #WOT=Webpage.objects.get(topic_name='Cricket')
    #WOT=Webpage.objects.get(topic_name='Foot Ball')
    WOT=Webpage.objects.all().order_by('name')#for ascending order
    WOT=Webpage.objects.all().order_by('-name')#for desending order
    WOT=Webpage.objects.all().order_by(Length('name'))# ascending according to length
    WOT=Webpage.objects.all().order_by(Length('name').desc())#desending according to length
    WOT=Webpage.objects.filter(name__startswith='k')
    WOT=Webpage.objects.filter(url__endswith='in')
    WOT=Webpage.objects.filter(name__contains='a')#it is used to get the name data if it contains 'a'
    WOT=Webpage.objects.filter(name__in=('Dhoni','Kholi'))
    WOT=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name='Dhoni'))# if we want to check multiple conditions then we have go for query object 'Q' in django.
    WOT=Webpage.objects.all()[:2]# to fetch first two rows.
    wd={'webpages':WOT}
    return render(request,'display_webpage.html',wd)

def display_ac(request):
    AOT=Accessrecord.objects.all()
    #In django >= and <= is not there because of that only we i'll go for field lookups
    AOT=Accessrecord.objects.filter(date__gt='1998-05-15')
    AOT=Accessrecord.objects.filter(date__gte='1998-05-15')
    AOT=Accessrecord.objects.filter(date__lt='1999-07-30')
    AOT=Accessrecord.objects.filter(date__lte='1999-07-30')
    AOT=Accessrecord.objects.filter(date__year='2000')#This fieldlookup is used compare with the help of year
    AOT=Accessrecord.objects.filter(date__month='7')
    AOT=Accessrecord.objects.filter(date__day='1')
    AOT=Accessrecord.objects.filter(date__month__gt='7')
    AOT=Accessrecord.objects.filter(date__month__gte='7')
    AOT=Accessrecord.objects.filter(date__year__lt='1999')
    AOT=Accessrecord.objects.filter(date__year__lte='1999')
    ad={'access':AOT}
    return render(request,'display_ac.html',ad)

def up_webpage(request):
    #Updation and Deletion Opertions
    #Webpage.objects.filter(name='Dhoni').update(email='finisher@gmail.com')
    #Webpage.objects.filter(topic_name='Cricket').update(url='http://cricket.com')
    #Webpage.objects.all().update(url='http://cricket.com')
    #Webpage.objects.update_or_create(topic_name='Cricket', defaults={'url':'http://cricket.com'})#It will error because by using Update_or_Create we can update only one row at a time.
    #Webpage.objects.update_or_create(name='Kholi', defaults={'email':'runmachine@gmail.com'})
    #TO=Topic.objects.get_or_create(topic_name='Cricket')[0]
    #TO.save()
    #Webpage.objects.update_or_create(name='hardhik', defaults={'topic_name':TO, 'name':'hardhik','url':'http://c.in','email':'hitter@gmail.com'})
    wd={'webpages':Webpage.objects.all()}
    return render(request,'display_webpage.html',wd)


def de_webpage(request):
    Webpage.objects.filter(name='kavitha').delete()
    Webpage.objects.filter(Q(topic_name='Foot Ball') | Q(topic_name='Kabadi')).delete()
    wd={'webpages':Webpage.objects.all()}
    return render(request,'display_webpage.html',wd)