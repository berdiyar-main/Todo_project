# Generated by Django 4.2.4 on 2023-08-26 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todomodel_created_alter_todomodel_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 26, 17, 38, 30, 146178)),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 26, 17, 38, 30, 146193)),
        ),
    ]
