# Generated by Django 2.1.1 on 2018-10-06 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BracketApp', '0019_auto_20181005_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='cum_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]