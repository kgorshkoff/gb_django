# Generated by Django 2.1.3 on 2019-02-03 19:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20190203_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='active_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 23, 19, 0, 20, 978562, tzinfo=utc)),
        ),
    ]
