# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
   
class Species(models.Model):
    is_active=models.BooleanField(default=False)
    specie_name = models.CharField(max_length=100,unique=True)


class Sources(models.Model):
    is_active=models.BooleanField(default=False)
    specie = models.ForeignKey(Species,related_name='sources',on_delete=models.CASCADE)
    source_name = models.CharField(max_length=100)


    class Meta:
        unique_together = ('specie', 'source_name')
        
    def __unicode__(self):
        return '%s' % (self.source_name)
        
class Process(models.Model):
    is_active=models.BooleanField(default=False)
    bwsize=models.CharField(max_length=15,default='')
    source=models.ForeignKey(Sources, related_name='process',on_delete=models.CASCADE)
    process_name=models.CharField(max_length=50,default='')
    citation=models.CharField(max_length=200,default='')
    gse=models.CharField(max_length=30,default='')
    gsm=models.CharField(max_length=15,default='')
    oganization=models.CharField(max_length=50,default='')
    pmid=models.CharField(max_length=30,default='')
    srr=models.CharField(max_length=15,default='')    
    submit_date=models.CharField(max_length=20,default='')
    tissue=models.CharField(max_length=15,default='')   
        
    def __unicode__(self):
        return '%s' % (self.process_name)

class GsmDetail(models.Model):
    gsm_id=models.CharField(max_length=15,default='')
    qc_trim_rate=models.CharField(max_length=5,default='')
    qc_mapping_rate=models.CharField(max_length=5,default='')
    qc_unique_mapping_rate=models.CharField(max_length=5,default='')
    qc_sequence_length=models.CharField(max_length=20,default='')
    qc_gc_rate=models.CharField(max_length=5,default='')
    qc_file_size=models.CharField(max_length=20,default='')
    tpm_0=models.IntegerField(default=0)
    tpm_0_1=models.IntegerField(default=0)
    tpm_1_10=models.IntegerField(default=0)
    tpm_10_100=models.IntegerField(default=0)
    tpm_100_1000=models.IntegerField(default=0)
    tpm_1000_10000=models.IntegerField(default=0)
    tpm_10000_100000=models.IntegerField(default=0)
    tpm_above_100000=models.IntegerField(default=0)
    tpm_top_5=models.CharField(max_length=300,default='')
    tpm_file_size=models.CharField(max_length=20,default='')
    nascent_number=models.IntegerField(default=0)
    nascent_intra=models.IntegerField(default=0)
    nascent_inter=models.IntegerField(default=0)
    nascent_below_100=models.IntegerField(default=0)
    nascent_100_1000=models.IntegerField(default=0)
    nascent_1000_5000=models.IntegerField(default=0)
    nascent_5000_10000=models.IntegerField(default=0)
    nascent_10000_50000=models.IntegerField(default=0)
    nascent_50000_100000=models.IntegerField(default=0)
    nascent_over_100000=models.IntegerField(default=0)
    nascent_file_size=models.CharField(max_length=20,default='')
    enhancer_number=models.IntegerField(default=0)
    enhancer_below_100=models.IntegerField(default=0)
    enhancer_100_500=models.IntegerField(default=0) 
    enhancer_500_1000=models.IntegerField(default=0)
    enhancer_1000_5000=models.IntegerField(default=0)
    enhancer_5000_9000=models.IntegerField(default=0)    
    enhancer_length_total=models.IntegerField(default=0)
    enhancer_file_size=models.CharField(max_length=20,default='')
    
    