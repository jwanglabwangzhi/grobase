# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import SpeciesView, print_example,file_download,GsmdetailView


urlpatterns = [
    url(r'^species_json/$', SpeciesView.as_view(), name='species-list'),
    url(r'^abc/$',print_example),
    url(r'^download/(.+)/$',file_download,name='file_download'),
    url(r'^gsm_detail_json/(.+)/$', GsmdetailView),
]
