# Generated by Django 2.0.1 on 2018-01-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GolferProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('handicap', models.IntegerField(default=18)),
                ('golf_club', models.CharField(max_length=255)),
                ('whats_in_your_bag', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]