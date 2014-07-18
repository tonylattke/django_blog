from django.db 			import models
from django.db.models  	import *
from datetime 			import datetime

class Post(models.Model):
	name  = models.CharField(max_length=200)
	text  = models.CharField(max_length=1000)
	date  = models.DateTimeField('Post date')

	class Meta:
		ordering = ['-date']

class Comment(models.Model):
	post = models.ForeignKey(Post)
	name = models.CharField(max_length=100)
	text = models.CharField(max_length=500)
	date = models.DateTimeField('Comment date')

	class Meta:
		ordering = ['-post','id']

	def post_tag(self):
		if self.post:
			return self.post.name
		else:
			return 'No Name'
	post_tag.short_description = 'Post name'
	post_tag.allow_tags = True