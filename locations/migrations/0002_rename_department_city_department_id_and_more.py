# Generated by Django 4.2.1 on 2023-06-04 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='department',
            new_name='department_id',
        ),
        migrations.RenameField(
            model_name='district',
            old_name='city',
            new_name='city_id',
        ),
    ]
