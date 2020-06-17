# Generated by Django 3.0.5 on 2020-05-21 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('class_master', '__first__'),
        ('school', '__first__'),
        ('student', '__first__'),
        ('teacher', '__first__'),
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('division_name', models.CharField(max_length=255)),
                ('division_desc', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.UserProfile')),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.School')),
            ],
        ),
        migrations.CreateModel(
            name='school_division_mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_master.class_master')),
                ('division_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='division.Division')),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
            ],
        ),
        migrations.CreateModel(
            name='teacher_class_mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('class_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher', verbose_name='teacher_id')),
                ('co_ordinator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.UserProfile')),
                ('school_division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='division.school_division_mapping')),
            ],
        ),
        migrations.CreateModel(
            name='student_class_mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('school_division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='division.school_division_mapping')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student', verbose_name='student_id')),
            ],
        ),
    ]
