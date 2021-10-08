from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from kipco import views


urlpatterns = [

    url(r'^processgoal/(?P<pk>[0-9]+)/$', views.processgoal_detail),
    url(r'^processgoal/$', views.processgoal_list),

    url(r'^activity/(?P<pk>[0-9]+)/$', views.activity_detail),
    url(r'^activity/$', views.activity_list),

    url(r'^activitygoal/(?P<pk>[0-9]+)/$', views.activitygoal_detail),
    url(r'^activitygoal/$', views.activitygoal_list),

    url(r'^intention/(?P<pk>[0-9]+)/$', views.intention_detail),
    url(r'^intention/$', views.intention_list),

    url(r'^desire/(?P<pk>[0-9]+)/$', views.desire_detail),
    url(r'^desire/$', views.desire_list),

    url(r'^agenttype/(?P<pk>[0-9]+)/$', views.agenttype_detail),
    url(r'^agenttype/$', views.agenttype_list),

    url(r'^agentspecialty/(?P<pk>[0-9]+)/$', views.agentspecialty_detail),
    url(r'^agentspecialty/$', views.agentspecialty_list),

    url(r'^agent/(?P<pk>[0-9]+)/$', views.agent_detail),
    url(r'^agent/$', views.agent_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
