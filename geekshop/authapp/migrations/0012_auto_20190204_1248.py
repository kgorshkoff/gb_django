# Generated by Django 2.1.3 on 2019-02-04 09:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0011_auto_20190203_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='active_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 9, 48, 20, 45717, tzinfo=utc)),
        ),
    ]
