# Generated by Django 3.1.2 on 2021-01-13 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurorsearch', '0020_userdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='toggle_favorites',
            field=models.BooleanField(default=False),
        ),
    ]
