from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __str__(self):
		return self.name


class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	view = models.IntegerField(default=0)

	def __str__(self):
		return self.title
