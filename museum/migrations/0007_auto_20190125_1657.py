# Generated by Django 2.1.5 on 2019-01-25 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0006_auto_20190115_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artwork',
            old_name='url',
            new_name='url_online',
        ),
    ]
