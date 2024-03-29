from django.db import models
from django.contrib.auth.models import User

# Location Type Choices
LOCATION_TYPES = [
	('Settlements', (
			('city', 'City'),
			('town', 'Town'),
			('village', 'Village'),
			('camp', 'Camp'),
		)
	),
	('Structures', (
			('castle', 'Castle'),
			('fort', 'Fort'),
			('tower', 'Tower'),
			('ruin', 'Ruin'),
			('house', 'House'),
			('misc structure', 'Misc Structure'),
		)
	),
	('Nature', (
			('mountain', 'Mountain'),
			('hill', 'Hill'),
			('valley', 'Valley'),
			('cavern', 'Cavern'),
			('wood', 'Wood'),
			('water', 'Water'),
			('misc landform', 'Misc Landform'),
		)
	),
	('Other', (
			('point of interest', 'Point of Interest'),
			('landmark', 'Landmark'),
			('other', 'Other'),
		)
	)
]
# Note: Nature section might end up including a LOT more -- depends on how granular we want to define them

LOCATION_SIZES = (
	('tiny', 'Tiny'),
	('small', 'Small'),
	('medium', 'Medium'),
	('large', 'Large'),
  	('huge', 'Huge'),
    ('gigantic', 'Gigantic'),
)

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
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	campaign = models.ForeignKey(Campaign, default=None, null=True, on_delete=models.SET_DEFAULT)
	name = models.CharField(max_length=100)
	description = models.TextField(default=None, null=True)
	def __str__(self):
		return self.name

class Map(models.Model):
	"""A Map that we can view on a page and interact with"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	image = models.ImageField(upload_to='upload/')
	campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Location(models.Model):
	"""A Location on a map, that we can point to"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	map = models.ForeignKey(Map, on_delete=models.CASCADE)
	size = models.CharField(
		max_length=10,
		choices = LOCATION_SIZES
	)
	type = models.CharField(
		max_length=25,
		choices=LOCATION_TYPES
	)
	title = models.CharField(max_length=200)
	text = models.TextField()
	xCoord = models.FloatField()
	yCoord = models.FloatField()

	def __str__(self):
		return self.title

class Note(models.Model):
	"""A note associated with a location"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	author = models.ForeignKey(Character, on_delete=models.CASCADE)
	location = models.ForeignKey(Location, on_delete=models.CASCADE) # Maybe we preserve the notes if a location is accidentally deleted?
	created = models.DateTimeField(auto_now_add=True)
	#updated = models.DateTimeField(auto_now=True)
	content = models.TextField()

	def __str__(self):
		return self.content