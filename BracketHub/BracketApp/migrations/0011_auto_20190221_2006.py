# Generated by Django 2.1.1 on 2019-02-22 04:06

from django.db import migrations
from django.utils import timezone

def add_datetime(apps, schema_editor):
    Season = apps.get_model('BracketApp', 'Season')
    for season in Season.objects.all():
        season.premiere = timezone.now()
        season.save()

class Migration(migrations.Migration):

    dependencies = [
        ('BracketApp', '0010_auto_20190221_1957'),
    ]

    operations = [
        migrations.RunPython(add_datetime),
    ]