# Generated by Django 2.2.6 on 2019-12-02 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_auto_20191202_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='delete',
            new_name='delet',
        ),
        migrations.RenameField(
            model_name='carrera',
            old_name='delete',
            new_name='delet',
        ),
    ]
