# Generated by Django 3.1.6 on 2021-02-08 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='last_update',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
