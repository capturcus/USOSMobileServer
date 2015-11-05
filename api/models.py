from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    usosid = models.IntegerField()

    class Meta:
        ordering = ('usosid',)