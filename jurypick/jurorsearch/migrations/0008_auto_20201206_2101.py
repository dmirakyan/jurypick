# Generated by Django 3.1.2 on 2020-12-06 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jurorsearch', '0007_auto_20201206_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='human',
            old_name='username',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='query',
            old_name='username',
            new_name='author',
        ),
    ]
