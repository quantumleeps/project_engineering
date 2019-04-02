# Generated by Django 2.2 on 2019-04-02 18:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20190402_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
