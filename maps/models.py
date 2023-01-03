from django.db import models
from django.contrib.auth.models import User

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

	LINEAGES = (
		('Aarakockra', 'Aaracokra'),
		('Aasimar', 'Aasimar'),
		('Bugbear', 'Bugbear'),
		('Centaur', 'Centaur'),
		('Changeling', 'Changeling'),
		('Dragonborn', 'Dragonborn'),
		('Dwarf', 'Dwarf'),
		('Elf', 'Elf'),
		('Fairy', 'Fairy'),
		('Firbolg', 'Firbolg'),
		('Air Genasi', ' Air Genasi'),
		('Earth Genasi', ' Earth Genasi'),
		('Fire Genasi', ' Fire Genasi'),
		('Water Genasi', ' Water Genasi'),
		('Gnome', 'Gnome'),
		('Goblin', 'Goblin'),
		('Golaith', 'Goliath'),
		('Half-Elf', 'Half-Elf'),
		('Half-Orc', 'Half-Orc'),
		('Halfling', 'Halfling'),
		('Harengon', 'Harengon'),
		('Human', 'Human'),
		('Kenku', 'Kenku'),
		('Lizardfolk', 'Lizardfolk'),
		('Orc', 'Orc'),
		('Tabaxi', 'Tabaxi'),
		('Tiefling', 'Tiefling'),
		('Tortle', 'Tortle'),
		('Warforged', 'Warforged'),
		('Yuan-Ti', 'Yuan-Ti')
	)

	LEVELS = (
		(1, '1'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5'),
		(6, '6'),
		(7, '7'),
		(8, '8'),
		(9, '9'),
		(10, '10'),
		(11, '11'),
		(12, '12'),
		(13, '13'),
		(14, '14'),
		(15, '15'),
		(16, '16'),
		(17, '17'),
		(18, '18'),
		(19, '19'),
		(20, '20')
	)
	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	campaign = models.ForeignKey(Campaign, default=None, null=True, on_delete=models.SET_DEFAULT)
	char_name = models.CharField(max_length=100)
	char_desc = models.TextField(default=None, null=True)
	char_lineage = models.CharField(max_length=32, choices=LINEAGES, null=True, default=None)
	char_class = models.CharField(max_length=32, choices=CLASSES, null=True, default=None)
	char_level = models.IntegerField(default=1, choices=LEVELS)

	def __str__(self):
		return self.char_name

class Map(models.Model):
	"""A Map that we can view on a page and interact with"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	map_title = models.CharField(max_length=50)
	map_image = models.ImageField(upload_to='upload/')
	campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

	def __str__(self):
		return self.map_title

class Location(models.Model):
	"""A Location on a map, that we can point to"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	map = models.ForeignKey(Map, on_delete=models.CASCADE)
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