# Generated by Django 3.2.3 on 2024-09-16 06:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cat',
            unique_together={('name', 'owner')},
        ),
    ]
