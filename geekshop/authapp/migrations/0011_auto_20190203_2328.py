# Generated by Django 2.1.3 on 2019-02-03 20:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_auto_20190203_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuserprofile',
            name='language',
            field=models.CharField(choices=[('ru', 'Русский'), ('en', 'English')], default='ru', max_length=20, verbose_name='язык'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='active_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 23, 20, 28, 28, 495741, tzinfo=utc)),
        ),
    ]
