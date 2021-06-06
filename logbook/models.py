from django.db import models

# Create your models here.

class Workweek(models.Model):
    week_num = models.IntegerField()
    image = models.FileField()

class Workday(models.Model):
    log = models.TextField()
    dt = models.DateField()
    week = models.ForeignKey(Workweek, on_delete=models.CASCADE)





