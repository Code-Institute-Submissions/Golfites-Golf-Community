# Generated by Django 2.0.1 on 2018-01-17 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ad_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='condition',
            field=models.CharField(default='', max_length=35),
        ),
    ]
