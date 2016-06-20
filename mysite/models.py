from django.db import models


class Activity(models.Model):
	title = models.CharField(max_length=20)
	content = models.CharField(max_length=100)	 
	image = models.FileField(null=True,blank=True)
	def __str__(self):
		return self.title

class Practice(models.Model):
	title = models.CharField(max_length=20)
	content = models.CharField(max_length=100)
	image = models.FileField(null=True,blank=True)	

	def __str__(self):
		return self.title
