# Generated by Django 2.2.2 on 2019-06-15 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dlfiles', '0003_auto_20190614_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='dlfile',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
