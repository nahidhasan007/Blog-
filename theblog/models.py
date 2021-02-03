from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	body = models.TextField()

	def __str__(self):
		return self.title + ' ' + str(self.author)

	def get_absolute_url(self):
		#return reverse('article_details',args={str(self.id)})
		return reverse('home')


class ovimot(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	c_body = models.TextField()

	def __str__(self):
		return self.post.title+ ' ' + self.name + ' ' + str(self.c_body)
		
