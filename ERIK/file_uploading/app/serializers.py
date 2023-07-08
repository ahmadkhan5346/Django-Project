from rest_framework import serializers
from app.models import EmployeesDetails


class RetrieveDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesDetails
        fields = ['id', 'emp_name', 'emp_city', 'emp_state', 'emp_designation', 'emp_date_of_joinning', 'emp_status', 'emp_salary']