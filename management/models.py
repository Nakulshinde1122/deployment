from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        db_table = "Emp-1"


class Address(models.Model):
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()
    empref = models.OneToOneField(Employee, on_delete=models.CASCADE)  # For 1-M use Foreignkey instead of OneToOneField
    # empref1 = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # empref2 = models.ManyToManyField(Employee)

    class Meta:
        db_table = "Address_01"
