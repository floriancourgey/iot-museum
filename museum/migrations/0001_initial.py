# Generated by Django 2.1.5 on 2019-01-09 04:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('edited_datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('url', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('timesPlayed', models.IntegerField(default=0)),
                ('origin', models.CharField(max_length=255)),
            ],
        ),
    ]
