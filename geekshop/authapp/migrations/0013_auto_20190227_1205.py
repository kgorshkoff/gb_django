# Generated by Django 2.1.3 on 2019-02-27 09:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_auto_20190204_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='active_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 16, 9, 5, 21, 792871, tzinfo=utc)),
        ),
    ]