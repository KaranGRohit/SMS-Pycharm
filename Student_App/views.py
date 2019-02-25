from django.shortcuts import render_to_response, render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponseRedirect
#import pymysql
from Student_App.models import Student
from django.template.context_processors import csrf
from django.views import generic
from Teacher_App.models import Attendance, Assignments, Result
from Principal_App.models import Timetable

class StudentListView(ListView):
	model = Student

class Mystudinfo(ListView):
    model = Student
    template_name = 'studentinfo.html'

class studinfo(DetailView):
    model = Student
    template_name = 'studdetails.html'
    context_object_name = 'batman'

def getstudentinfo(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('addstudentinfo.html', c)


def viewattendance(request):
    myattendance = Attendance.objects.order_by('Roll_no')
    ctx = {'myattendance':myattendance}
    return render(request, 'viewattendance.html', ctx)

def viewresult(request):
    myresult = Result.objects.order_by('Roll_no')
    ctx = {'myresult':myresult}
    return render(request, 'viewresult.html', ctx)

def viewassignment(request):
    myassignment = Assignments.objects.order_by('assingment')
    ctx = {'myassignment':myassignment}
    return render(request, 'viewassignments.html',ctx)

def viewtimetable(request):
    mytimetable = Timetable.objects.order_by('room_no')
    ctx = {'mytimetable':mytimetable}
    return render(request, 'viewtimetable.html',ctx)

#def studentinfo(request):
#    return render_to_response('studentinfo.html')

def addstudentinfo(request):
    sfname = request.POST.get('sfname', '')
    slname = request.POST.get('slname', '')
    saddr = request.POST.get('saddr', '')
    semail = request.POST.get('semail', '')
    sclass = request.POST.get('sclass', '')
    s = Student(SFName=sfname, SLname=slname, SAddress=saddr, SEmail=semail, SClass=sclass)
    s.save()

    res = 'Printing all Student entries in the DB : <br>'

    return HttpResponseRedirect('student/addsuccess/')


def addsuccess(request):
	return render_to_response('addrecord.html')
