# Generated by Django 3.1 on 2020-10-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pro_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
    ]
