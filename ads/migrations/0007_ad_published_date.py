# Generated by Django 2.0.1 on 2018-01-30 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_remove_ad_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
