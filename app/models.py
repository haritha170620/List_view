from django.db import models

# Create your models here.

class Trainer(models.Model):
    trainer_name=models.CharField(max_length=100,primary_key=True)
    age=models.IntegerField()
    subject=models.CharField(max_length=100)
