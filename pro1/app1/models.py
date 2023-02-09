from django.db import models

class Employee(models.Model):
    eid = models.IntegerField()
    name = models.CharField(max_length=90)
    age = models.IntegerField()
    city = models.CharField(max_length=90)
