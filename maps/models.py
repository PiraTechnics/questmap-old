from django.db import models

class Map(models.Model):
	"""A Map that we can view on a page and interact with"""
	map_title = models.CharField(max_length=50)
	map_image = models.ImageField(upload_to='upload/', 
		width_field='image_width', height_field='image_height')
	image_height = models.IntegerField()
	image_width = models.IntegerField()

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