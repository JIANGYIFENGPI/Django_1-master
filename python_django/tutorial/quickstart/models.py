# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
	movieName = models.CharField(max_length=45)
	Director = models.CharField(max_length=100)
	publish_date = models.DateField()
	
	def __str__(self):
		return self.movieName
