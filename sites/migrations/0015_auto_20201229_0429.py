# Generated by Django 3.1.2 on 2020-12-29 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0014_auto_20201229_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='sub_tag',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='sites.subtags'),
        ),
    ]
