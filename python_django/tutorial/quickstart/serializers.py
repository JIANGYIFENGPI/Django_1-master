from django.contrib.auth.models import User
from models import  Course, Curriculum, Group, Implement, Subgroup, Room, Teacher, 
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'id','code', 'courseid','name', 'language', 'cr','roomid','teacher','degreeprogram','numberofgroup','teachingyear','groupid', 'curriculumid')
		
class CurriculumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curriculum
        fields = ('url', 'id','numberofgroup','courseid')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','id','code', 'degree program','implementid')
		
class ImplementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Implement
        fields = ('url', 'id','p1','p2','p3','p4','p5','period','startdate','enddate','teacherid','courseid')
		
class GroupCourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupCourse
        fields = ('url', 'id','code','degree program', 'implementid')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('url', 'id', 'room seats', 'topic','courseid')

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url','id','code','name')
		
