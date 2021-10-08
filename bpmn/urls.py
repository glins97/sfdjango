from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bpmn import views


urlpatterns = [

    url(r'^flowelement/(?P<pk>[0-9]+)/$', views.flowelement_detail),
    url(r'^flowelement/$', views.flowelement_list),

    url(r'^flownode/(?P<pk>[0-9]+)/$', views.flownode_detail),
    url(r'^flownode/$', views.flownode_list),

    url(r'^sequenceflow/(?P<pk>[0-9]+)/$', views.sequenceflow_detail),
    url(r'^sequenceflow/$', views.sequenceflow_list),

    url(r'^activity/(?P<pk>[0-9]+)/$', views.activity_detail),
    url(r'^activity/$', views.activity_list),

    url(r'^flowelementscontainer/(?P<pk>[0-9]+)/$', views.flowelementscontainer_detail),
    url(r'^flowelementscontainer/$', views.flowelementscontainer_list),

    url(r'^process/(?P<pk>[0-9]+)/$', views.process_detail),
    url(r'^process/$', views.process_list),

    url(r'^task/(?P<pk>[0-9]+)/$', views.task_detail),
    url(r'^task/$', views.task_list),

    url(r'^subprocess/(?P<pk>[0-9]+)/$', views.subprocess_detail),
    url(r'^subprocess/$', views.subprocess_list),

    url(r'^eventtype/(?P<pk>[0-9]+)/$', views.eventtype_detail),
    url(r'^eventtype/$', views.eventtype_list),

    url(r'^event/(?P<pk>[0-9]+)/$', views.event_detail),
    url(r'^event/$', views.event_list),

    url(r'^laneset/(?P<pk>[0-9]+)/$', views.laneset_detail),
    url(r'^laneset/$', views.laneset_list),

    url(r'^lane/(?P<pk>[0-9]+)/$', views.lane_detail),
    url(r'^lane/$', views.lane_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
