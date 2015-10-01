from django.db import models

class farmer(models.Model):
    Firstname = models.CharField(max_length=200)
    Lastname= models.CharField(max_length=200)
    Othername=models.CharField(max_length=200)
    DOB=models.DateTimeField('date born')
    Gender=models.CharField(max_length=8)
    IdType=models.CharField(max_length=200)
    IdNumber=models.CharField(max_length=200)
    FarmArea=models.CharField(max_length=200)
    FarmAreaDimensions=models.CharField(max_length=200)
    ZoneId=models.CharField(max_length=200)
    BlockId=models.CharField(max_length=200)
    CampId=models.CharField(max_length=200)
    DistrictId=models.CharField(max_length=200)
    FarmAreaId=models.CharField(max_length=200)

# Create your models here.
