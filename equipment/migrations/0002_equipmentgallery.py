# Generated by Django 2.0.1 on 2018-01-18 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images', verbose_name='images')),
                ('countries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='equipment.Equipment')),
            ],
        ),
    ]