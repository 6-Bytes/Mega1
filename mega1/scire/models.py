from django.db import models

class team(models.Model):
    lead= models.CharField(max_length=255)
    member=models.CharField(max_length=255)
# Create your models here.
