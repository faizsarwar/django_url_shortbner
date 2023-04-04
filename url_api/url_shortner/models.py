from django.db import models

# Create your models here.
class url_data(models.Model):
    title= models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    img= models.CharField(max_length=355)
    link= models.CharField(max_length=400)
    link_counter =  models.IntegerField(default=0)
    class_id = models.IntegerField(default=0)
    instance_id = models.IntegerField(default=0)
    substrate_address =  models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)