from django.urls import re_path
from django.contrib import admin

from .views import (UserCreateAPIView,)

app_name = 'account'

urlpatterns =[
    re_path(r'^register/$', UserCreateAPIView.as_view(), name = 'register'),
    # re_path(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    # re_path(r'^register/$', UserCreateAPIView.as_view(), name='register'),
]








