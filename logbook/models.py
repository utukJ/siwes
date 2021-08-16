from django.db import models
from accounts.models import Student

# Create your models here.



class Workweek(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    week_num = models.IntegerField(default=0)
    image = models.FileField(default=None)
    start_date = models.DateField()
    d1 = models.TextField(default="", verbose_name="Monday")
    d2 = models.TextField(default="", verbose_name="Tuesday")
    d3 = models.TextField(default="", verbose_name="Wednesday")
    d4 = models.TextField(default="", verbose_name="Thursday")
    d5 = models.TextField(default="", verbose_name="Friday")

    def __str__(self):
        return "week " + str(self.week_num) + ", " + self.author.__str__()