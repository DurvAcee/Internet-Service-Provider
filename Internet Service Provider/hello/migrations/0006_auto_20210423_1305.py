# Generated by Django 3.0.5 on 2021-04-23 07:35

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='accno',
            field=models.CharField(default=datetime.datetime(2021, 4, 23, 7, 34, 55, 399653, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='email',
            field=models.CharField(default=datetime.datetime(2021, 4, 23, 7, 35, 10, 879632, tzinfo=utc), max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='mob',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='planid',
            field=models.CharField(default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
    ]
