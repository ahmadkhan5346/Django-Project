from django.db import models

# Create your models here.


class Catalyst(models.Model):
    company_number = models.IntegerField()
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    year_founded = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    range = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    linked_in_url = models.CharField(max_length=100)
    current_employee_estimate = models.CharField(max_length=100)
    total_employee_estimate = models.CharField(max_length=100)