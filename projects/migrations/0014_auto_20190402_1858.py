# Generated by Django 2.2 on 2019-04-02 18:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20190402_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
    ]