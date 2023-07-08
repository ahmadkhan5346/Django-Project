from django.db import models


class EmployeesDetails(models.Model):
    emp_name = models.CharField(max_length=50, unique=True, null=False)
    emp_city = models.CharField(max_length=50)
    emp_state = models.CharField(max_length=50)
    emp_designation = models.CharField(max_length=50, null=False)
    emp_date_of_joinning = models.DateField(null=False)
    emp_status = models.CharField(max_length=50)
    emp_salary = models.CharField(max_length=50, null=False)
