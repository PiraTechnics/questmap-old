from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Campaign(models.Model):
	"""A campaign that characters and maps are in.
	Basically, the a representation of the instance of a game
	that is owned by a GM user, and played in by a number of player users
	represented by their respective characters"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.title

class Character(models.Model):
	"""A Character that goes on adventures, and their info"""
	CLASSES = (
		('Artificer', 'Artificer'),
		('Barbarian', 'Barbarian'),
		('Bard', 'Bard'),
		('Cleric', 'Cleric'),
		('Druid', 'Druid'),
		('Fighter', 'Fighter'),
		('Monk', 'Monk'),
		('Paladin', 'Paladin'),
		('Ranger', 'Ranger'),
		('Rogue', 'Rogue'),
		('Sorcerer', 'Sorcerer'),
		('Warlock', 'Warlock'),
		('Wizard', 'Wizard')
	)
	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	# Can't migrate this without causing "non null integrity errors" so hang off for now
	#campaign = models.ForeignKey(Campaign, null=True, default=None, on_delete=models.SET_DEFAULT)
	char_name = models.CharField(max_length=100)
	char_desc = models.TextField(default=None, null=True)
	char_class = models.CharField(max_length=32, choices=CLASSES, null=True, default=None)
	char_level = models.IntegerField(default=1,validators=[MaxValueValidator(20), MinValueValidator(1)])

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