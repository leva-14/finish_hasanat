# Generated by Django 3.1.2 on 2020-12-27 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0009_auto_20201225_0522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images_news',
            name='sub_title',
        ),
        migrations.RemoveField(
            model_name='images_news',
            name='title',
        ),
    ]
