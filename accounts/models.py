from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from datetime import date

# Create your models here.

class Student(AbstractBaseUser):
    matric = models.CharField(max_length=9, blank=False, null=False)
    sws_start_date = models.DateField(default=date.today())
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_email = models.EmailField(blank=True, null=True)

    USERNAME_FIELD = 'matric'
    EMAIL_FIELD = 'user_email'
    REQUIRED_FIELDS = ['user_email', 'first_name', 'last_name']

    def __str__(self):
        return self.first_name + " " + self.last_name + self.matric

class StudentManager(BaseUserManager):

    pass





