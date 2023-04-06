from django.db import models

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=100)
    price = models.IntegerField(null=False,default=0)

