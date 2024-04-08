# Generated by Django 5.0.4 on 2024-04-08 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('answers', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Assessment_Areas',
            fields=[
                ('assessment_area', models.CharField(max_length=255)),
                ('assessment_area_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Correct_answer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_name', models.CharField(max_length=255)),
                ('school_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.IntegerField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=255)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_data.school')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_data.class')),
            ],
        ),
    ]
