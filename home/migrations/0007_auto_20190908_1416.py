# Generated by Django 2.2 on 2019-09-08 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190908_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 14, 16, 15, 183835)),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 14, 16, 15, 183835)),
        ),
    ]
