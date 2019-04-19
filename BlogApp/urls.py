
from django.contrib import admin
from django.urls import re_path, include
from account.views import (login_view, register_view, logout_view)

app_name = 'account'

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^login/', login_view, name='login'),
    re_path(r'^logout/', logout_view, name='logout'),
    re_path(r'^register/', register_view, name='register'),
    re_path(r'^', include('post.urls', namespace='post')),
    re_path(r'^api/users/', include('account.api.urls', namespace='users-api')),
    re_path(r'^api/post/', include('post.api.urls', namespace='post-api')),
]
