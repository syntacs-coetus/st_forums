# Generated by Django 3.0.2 on 2020-01-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200128_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_address',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterModelTable(
            name='profile',
            table='user_profiles',
        ),
    ]
