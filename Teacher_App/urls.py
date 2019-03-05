
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('', views.Myteacher.as_view(),name='teacher'),
    path('uploadresult/',views.uploadresult, name='uploadresult'),
    path('teacherinfo/', views.teacherpage.as_view(), name='home'),
]
