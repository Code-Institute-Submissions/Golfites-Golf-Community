# Generated by Django 2.0.1 on 2018-01-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('course_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('url', models.URLField(null=True)),
                ('contact_number', models.CharField(default='', max_length=60)),
                ('course_description', models.TextField(default='')),
            ],
        ),
    ]
