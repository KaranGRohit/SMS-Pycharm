from django.urls import path
from . import views

from django.conf.urls import url

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    url(r'^getstudentinfo/addstudentinfo/', views.addstudentinfo),
    url(r'^getstudentinfo/', views.getstudentinfo),
    path('', views.Mystudinfo.as_view(),name='studentinfo'),
    path('studinfo/', views.studinfo.as_view(), name='student_page'),
    url(r'^addsuccess/', views.addsuccess),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('viewattendance/', views.viewattendance),
    path('viewresult/', views.viewresult),
    path('viewassignments/', views.viewassignment),
    path('viewtimetable/', views.viewtimetable),

]
