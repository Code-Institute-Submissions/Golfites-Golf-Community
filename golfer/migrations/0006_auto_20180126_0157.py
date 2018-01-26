# Generated by Django 2.0.1 on 2018-01-26 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0005_auto_20180126_0054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='golferprofile',
            old_name='swing',
            new_name='swing_video',
        ),
        migrations.RenameField(
            model_name='golferprofile',
            old_name='golf_club',
            new_name='your_golf_club',
        ),
        migrations.RenameField(
            model_name='golferprofile',
            old_name='image',
            new_name='your_image',
        ),
        migrations.RenameField(
            model_name='golferprofile',
            old_name='name',
            new_name='your_name',
        ),
        migrations.AlterField(
            model_name='golferprofile',
            name='golfer',
            field=models.ForeignKey(blank=True, default='user.username', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
