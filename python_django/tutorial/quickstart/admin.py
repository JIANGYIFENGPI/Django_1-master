# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import Course, Curriculum, Group, Implement, Subgroup, Room, Teacher



admin.site.register(Course)
admin.site.register(Curriculum)
admin.site.register(Group)
admin.site.register(Implement)
admin.site.register(Sugroup)
admin.site.register(Room)
admin.site.register(Teacher)
