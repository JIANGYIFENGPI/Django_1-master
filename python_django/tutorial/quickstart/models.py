# -*- coding: utf-8 -*-
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models


class Course(models.Model):
	id = models.IntegerField(db_column='id')
	courseid = models.IntegerField(db_column='id')
    code = models.CharField(unique=True, max_length=10)
    name = models.CharField(max_length=50)
	degree program = models.CharField(max_length=50)
    numberofgroup= models.CharField(max_length=50)
    language = models.CharField(max_length=10)
    cr = models.IntegerField()
	teachingyear= models.IntegerField()
    curriculumid = models.ForeignKey('Curriculum', models.DO_NOTHING, db_column='curriculumid')  # Field name made lowercase.
	groupid = models.ForeignKey('group', models.DO_NOTHING, db_column='groupid')  # Field name made lowercase.
	roomid = models.ForeignKey('group', models.DO_NOTHING, db_column='roomid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course'


class Implement(models.Model):
	id = models.IntegerField(db_column='id')
    p1 = models.IntegerField(db_column='P1', blank=True, null=True)  # Field name made lowercase.
    p2 = models.IntegerField(db_column='P2', blank=True, null=True)  # Field name made lowercase.
    p3 = models.IntegerField(db_column='P3', blank=True, null=True)  # Field name made lowercase.
    p4 = models.IntegerField(db_column='P4', blank=True, null=True)  # Field name made lowercase.
    p5 = models.IntegerField(db_column='P5', blank=True, null=True)  # Field name made lowercase.
	period= models.IntegerField(db_column='period')  # Field renamed to remove unsuitable characters.
    startdate= models.IntegerField(db_column='startdate', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    enddate= models.IntegerField(db_column='enddate', blank=True, null=True)  # Field renamed to remove unsuitable characters.
	Teacherid= models.IntegerField(db_column='Teacherid', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    courseid = models.IntegerField(db_column='courseid', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Implement'


class Group(models.Model):
	id = models.IntegerField(db_column='id')
    code = models.CharField(unique=True, max_length=10)
    degreeprogram = models.CharField(db_column='degree program', max_length=5)  # Field renamed to remove unsuitable characters.
	implementid = models.IntegerField(db_column='implementid', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'group'


class Subgroup(models.Model):
	id = models.IntegerField(db_column='id')
	code = models.CharField(unique=True, max_length=10)
    groupid = models.ForeignKey(Group, models.DO_NOTHING, db_column='groupid', primary_key=True)
    
    class Meta:
        managed = False
        db_table = 'Subgroup'
        unique_together = (('groupid', 'courseid'),)


class curriculum(models.Model):
    id = models.IntegerField(db_column='id')
	numberofgroup= models.CharField(max_length=50)
	courseid = models.IntegerField(db_column='courseid', blank=True, null=True)  # Field renamed to remove unsuitable characters.

	

    class Meta:
        managed = False
        db_table = 'curriculum'





class Room(models.Model):
    id = models.IntegerField(db_column='id')
	room seats = models.CharField(unique=True, max_length=10)
    topic = models.CharField(max_length=20)
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'


class Teacher(models.Model):
	id = models.IntegerField(db_column='id')
    code = models.CharField(unique=True, max_length=5)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'teacher'