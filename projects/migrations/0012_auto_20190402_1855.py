# Generated by Django 2.2 on 2019-04-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20190402_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='taggedequipment',
            name='code',
            field=models.CharField(max_length=40),
        ),
    ]
