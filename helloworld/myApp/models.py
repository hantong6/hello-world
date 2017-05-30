from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name=models.CharField(max_length=20)
    passwd=models.CharField(max_length=20)
    def __str__(self):
        return self.name.encode("utf-8")