from django.urls import re_path
from .import views


app_name = 'polls'

urlpatterns =[
    re_path(r'^$', views.PostListView.as_view(), name='post'),
    # re_path(r'^create/$', views.post_create, name='create'),
    # re_path(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
    # re_path(r'^(?P<id>\d+)/update/$', views.post_update, name='update'),
    # re_path(r'^(?P<id>\d+)/delete/$', views.post_delete, name='delete')

]



















