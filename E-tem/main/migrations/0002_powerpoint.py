# Generated by Django 2.1.15 on 2020-08-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Powerpoint',
            fields=[
                ('img_src', models.URLField()),
                ('download_link', models.TextField(blank=True, null=True)),
                ('detail_page', models.TextField(blank=True, null=True)),
                ('color_tag', models.TextField(blank=True, null=True)),
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'pptbizcam_real',
                'managed': False,
            },
        ),
    ]
