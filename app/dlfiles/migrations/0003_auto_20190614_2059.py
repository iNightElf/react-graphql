# Generated by Django 2.2.2 on 2019-06-14 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dlfiles', '0002_auto_20190614_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dlfile',
            name='downloadable_till',
        ),
        migrations.RemoveField(
            model_name='dlfile',
            name='posted_by',
        ),
    ]
