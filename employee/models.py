from django.db import models

# Create your models here.

class Department(models.Model):
    department_id=models.CharField(max_length=20)
    department_name=models.CharField(max_length=50)
    department_email=models.EmailField()
    
    def get_department_size(self):
        return self.employee_set.count()
    
    def __str__(self):
        return self.department_name


class Employee(models.Model):
    employee_id=models.CharField(max_length=20)
    employee_name=models.CharField(max_length=90)
    employee_email=models.EmailField()
    employee_contact=models.CharField(max_length=10)
    employee_department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.employee_name
    
