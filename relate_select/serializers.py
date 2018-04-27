# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Species, Sources, Process, GsmDetail
#from .models import Album,Track


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = "__all__"          

class SourcesSerializer(serializers.ModelSerializer):
    process = ProcessSerializer(many=True, read_only=True)
    class Meta:
        model = Sources
        fields = "__all__"       

class SpeciesSerializer(serializers.ModelSerializer):
    sources = SourcesSerializer(many=True, read_only=True)
    class Meta:
        model = Species
        fields = "__all__"       
        
class GsmdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GsmDetail
        fields = "__all__"           
'''
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('order', 'title', 'duration')

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')
'''        