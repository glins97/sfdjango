from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from agent import views



urlpatterns = [
    url(r'^sendmsg/$', views.sendMsg),
]

urlpatterns = format_suffix_patterns(urlpatterns)