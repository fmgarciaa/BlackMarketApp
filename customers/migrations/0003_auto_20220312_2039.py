# Generated by Django 3.1 on 2022-03-13 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20220312_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='is_regular_client',
            field=models.BooleanField(default=0),
        ),
    ]
