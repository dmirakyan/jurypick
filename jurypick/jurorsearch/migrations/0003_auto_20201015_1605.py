# Generated by Django 3.1.2 on 2020-10-15 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jurorsearch', '0002_auto_20201015_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='address',
        ),
        migrations.RemoveField(
            model_name='query',
            name='city',
        ),
        migrations.RemoveField(
            model_name='query',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='query',
            name='state',
        ),
    ]
