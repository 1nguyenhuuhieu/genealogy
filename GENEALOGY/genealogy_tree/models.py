from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    SEX_CHOICES = [
        ('male', 'Nam'),
        ('female', 'Nữ'),
    ]
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    birth_date = models.DateField(blank=True)

class FamilyLine(models.Model):
    sur_name = models.CharField(max_length=200)
    
class Address(models.Model):
    province_id = models.IntegerField()
    district_id = models.IntegerField()
    commune_id = models.IntegerField()


