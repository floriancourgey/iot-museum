# Generated by Django 2.1.5 on 2020-08-08 18:46

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('museum', '0016_auto_20200808_1840'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='GameUser',
        ),
    ]