# Generated by Django 5.1 on 2025-02-16 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='appointment_type',
            new_name='appointment_types',
        ),
    ]
