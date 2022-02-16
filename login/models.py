from django.db import models

# Create your models here.


class login_details(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'LOGIN_MASTER'
