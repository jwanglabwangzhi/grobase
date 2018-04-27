# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer

from .models import Species,GsmDetail
from .serializers import SpeciesSerializer,GsmdetailSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class SpeciesView(ListAPIView):
    """
    Returns a list of all .
    """
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

def GsmdetailView(request,param):
    """
    Returns a list of all .
    """

    try:
        queryset = GsmDetail.objects.get(gsm_id=param)
    except queryset.DoesNotExist:
        return HttpResponse(status=404) 
        
    if request.method == 'GET':
        serializer = GsmdetailSerializer(queryset)
        return JSONResponse(serializer.data)        

    
    
def print_example(request):
    return render(request, 'index.html')


    
from django.http import FileResponse  
def file_download(request,file_name):
    #author_id=request.user.id
    #created=request.POST.get("created","")
    #filename=request.POST.get("files","")
    
    #fire_dir='e:/media/'+str(created_time)+'/'+str(author_id)+'/'
    #file=open(fire_dir+file_name,'rb') 
    file_dir='e:/media/grobase/'+str(file_name)
    file=open(file_dir,'rb')
    response =FileResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="%s"'%file_name.split('/')[-1] 
    return response  
