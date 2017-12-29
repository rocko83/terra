from django.db import models
import src.azure
# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=255, null=False)
    filedata = models.CharField(max_length=255, null=True)
    creation = models.DateField()
    cloud_id = models.IntegerField()