
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('account/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('signup/', views.signup, name='signup')
]
