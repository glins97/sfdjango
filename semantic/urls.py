from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from semantic import views



urlpatterns = [
    url(r'^query/$', views.querySPARQ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
