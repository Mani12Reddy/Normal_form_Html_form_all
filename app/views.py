from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse 

def insert_topic(request):

    if request.method=='POST':
        tn=request.POST['topic']
        t=Topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        return HttpResponse('topic insert sucessfully!!!!')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    if request.method=='POST':
        to=request.POST['to']
        na=request.POST['na']
        ur=request.POST['ur']
        t=Topic.objects.get_or_create(topic_name=to)[0]
        t.save()
        w=Webpage.objects.get_or_create(topic_name=t,name=na,url=ur)[0]
        w.save()
        return HttpResponse('webpage insert ucessfully!!')

    return render(request,'insert_webpage.html',d)


def access(request):
    webpages=Webpage.objects.all()
    d={'webpages':webpages}

    if request.method=='POST':
        na=request.POST['na']
        dt=request.POST['dt']
        w=Webpage.objects.get_or_create(name=na)[0]
        w.save()
        a=AccessRecords.objects.get_or_create(name=w,data=dt)[0]
        a.save()
        return HttpResponse('accessRecords insert sucessfully!!!!')
    return render(request,'access.html',d)


def display_webpages(request):
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)


def select_topic(request):

    topics=Topic.objects.all()
    T={'topics':topics}

    if request.method=='POST':
        t=request.POST.getlist('topic')
        print(t)
        webpages=Webpage.objects.none()
        for i in t:
            webpages=webpages|Webpage.objects.filter(topic_name=i)
            data={'webpages':webpages}
            return render(request,'display_webpages.html',data)


    return render(request,'select_topic.html',T)


def check_box(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    return render(request,'check_box.html',d)