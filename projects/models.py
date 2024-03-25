from django.db import models

# Create your models here.

class Project(models.Model):
    documents = models.FileField(upload_to='')
    amount = models.IntegerField()
    status = models.BooleanField(default=False)
    into = models.BooleanField(default=False)
    photo = models.FileField(upload_to='')
    category = models.CharField(max_length=255)
    props = models.CharField(max_length=255)

