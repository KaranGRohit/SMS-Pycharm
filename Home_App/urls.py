
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts/urls'))
]
