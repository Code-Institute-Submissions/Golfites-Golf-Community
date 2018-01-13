# Generated by Django 2.0.1 on 2018-01-11 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0004_golferprofile_about_my_golf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='golferprofile',
            old_name='handicap',
            new_name='current_handicap',
        ),
        migrations.AddField(
            model_name='golferprofile',
            name='biggest_golfing_achievement',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='golferprofile',
            name='lowest_handicap',
            field=models.IntegerField(default=18),
        ),
        migrations.AlterField(
            model_name='golferprofile',
            name='whats_in_your_bag',
            field=models.TextField(blank=True, default='', max_length=600, null=True),
        ),
    ]