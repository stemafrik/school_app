# Generated by Django 3.0.5 on 2020-06-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20200601_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school_logo',
            field=models.FileField(blank=True, upload_to='media/school/'),
        ),
    ]
