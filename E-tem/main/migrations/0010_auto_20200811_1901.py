# Generated by Django 2.2.9 on 2020-08-11 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='count',
            old_name='count',
            new_name='counts',
        ),
    ]
