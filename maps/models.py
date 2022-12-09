from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
	"""A Character that goes on adventures, and their info"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	char_name = models.CharField(max_length=75)

	def __str__(self):
		return self.char_name

class Map(models.Model):
	"""A Map that we can view on a page and interact with"""
	map_title = models.CharField(max_length=50)
	map_image = models.ImageField(upload_to='upload/')

	def __str__(self):
		return self.map_title

class Location(models.Model):
	"""A Location on a map, that we can point to"""
	map = models.ForeignKey(Map, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	xCoord = models.IntegerField()
	yCoord = models.IntegerField()

	def __str__(self):
		return self.title

class Note(models.Model):
	"""A note associated with a location"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	author = models.CharField(max_length=100, default='Anon E. Mouse')
	created = models.DateTimeField(auto_now_add=True)
	#updated = models.DateTimeField(auto_now=True)
	content = models.TextField()

	def __str__(self):
		return self.content