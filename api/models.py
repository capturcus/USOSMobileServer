from django.db import models

# Create your models here.

class Student(models.Model):
    deviceid = models.CharField(max_length=100)
    usosid = models.IntegerField()

    class Meta:
        ordering = ('usosid',)
