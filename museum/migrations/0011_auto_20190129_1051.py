# Generated by Django 2.1.5 on 2019-01-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0010_artwork_date_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='author',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
