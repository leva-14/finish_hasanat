# Generated by Django 3.1.2 on 2020-12-30 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0019_сonsultation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сonsultation',
            name='number_phone',
            field=models.IntegerField(),
        ),
    ]