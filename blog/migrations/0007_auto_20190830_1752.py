# Generated by Django 2.2.2 on 2019-08-30 12:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190830_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='appointment_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
