# Generated by Django 2.2.6 on 2019-11-28 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_carrera'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='email',
            field=models.CharField(default='email', max_length=70),
        ),
        migrations.AddField(
            model_name='alumno',
            name='password',
            field=models.CharField(default='password', max_length=30),
        ),
    ]
