# Generated by Django 3.1.2 on 2020-12-30 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0020_auto_20201230_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сonsultation',
            name='number_phone',
            field=models.CharField(max_length=255),
        ),
    ]
