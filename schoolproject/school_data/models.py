from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=255)
    school_id = models.IntegerField(primary_key=True)

class Class(models.Model):
    class_id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=255)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=255)

class Assessment_Areas(models.Model):
    assessment_area = models.CharField(max_length=255)
    assessment_area_id = models.IntegerField(primary_key=True)

class Awards(models.Model):
    award = models.CharField(max_length=255)

class Answers(models.Model):
    id = models.IntegerField(primary_key=True)
    answers = models.CharField(max_length=255)
