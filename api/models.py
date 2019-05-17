from django.contrib.auth.models import User
from django.db import models
from jsonfield import JSONField

# Create your models here.
class Skrypt(models.Model):
    identifier = models.CharField(max_length=50)
    course_name = models.CharField(max_length=12)
    data = models.CharField(max_length=30)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.identifier

class Data(models.Model):
    identifier = models.CharField(max_length=50)
    data = JSONField()

    def __str__(self):
        return self.identifier