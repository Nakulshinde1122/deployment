# Generated by Django 2.2.9 on 2022-01-19 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(default='Pune', max_length=250),
        ),
    ]
