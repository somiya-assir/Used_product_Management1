# Generated by Django 3.1 on 2020-09-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=100)),
                ('contact_no', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
