# Generated by Django 5.1.1 on 2024-10-07 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0003_alter_classroom_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='department',
        ),
    ]
