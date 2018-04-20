from django.db import models

# Create your models here.
class Caosmonkey(models.Model):
    name = models.CharField(max_length=255, null=False)
    filedata = models.CharField(max_length=255, null=False)
    creation = models.DateField()
    cloud_id = models.IntegerField()
    lastExecution = models.DateField()
    enabled = models.BooleanField()
    id = models.AutoField(primary_key=True)