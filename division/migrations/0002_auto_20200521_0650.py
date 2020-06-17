# Generated by Django 3.0.5 on 2020-05-21 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_class_mapping',
            name='school_division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='division.school_division_mapping'),
        ),
    ]
