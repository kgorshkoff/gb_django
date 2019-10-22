# Generated by Django 2.1.3 on 2019-02-03 19:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20190203_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(blank=True, max_length=128, verbose_name='тэги')),
                ('about_me', models.TextField(blank=True, max_length=512, verbose_name='о себе')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Мужчина'), ('W', 'Женщина')], max_length=1, verbose_name='пол')),
            ],
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='active_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 23, 19, 32, 5, 881210, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='shopuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]