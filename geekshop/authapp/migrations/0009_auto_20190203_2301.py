# Generated by Django 2.1.3 on 2019-02-03 20:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20190203_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='active_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 23, 20, 1, 54, 355619, tzinfo=utc)),
        ),
    ]
