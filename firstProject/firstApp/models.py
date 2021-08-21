from django.db import models

# Create your models here.

class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    sal=models.DecimalField(max_digits=20,decimal_places=3)
