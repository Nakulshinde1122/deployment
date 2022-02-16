from django.db import models

# Create your models here.


class Employee(models.Model):
    # id = models.IntegerField()
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=300, default='Guest')
    phone_number = models.BigIntegerField(unique=True)
    joining_date = models.DateField()
    address = models.CharField(max_length=250, default='Pune')

    class Meta:
        db_table = 'EMPLOYEE_MASTER'
        ordering = ['role']
