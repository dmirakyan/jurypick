# Generated by Django 3.1.2 on 2020-10-30 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurorsearch', '0003_auto_20201015_1605'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Human',
        ),
        migrations.AddField(
            model_name='query',
            name='address',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='birth_date',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='city',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='email',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='middle_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='phone',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='query',
            name='state',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='first_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='last_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='zip_code',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
