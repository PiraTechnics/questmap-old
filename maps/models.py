from django.db import models

class Map(models.Model):
	"""A Map that we can view on a page and interact with"""
	map_title = models.CharField(max_length=50)
	map_image = models.ImageField(upload_to='upload/')
	#height = models.IntegerField(map_image.height_field)
	#width = models.IntegerField(map_image.width_field)

	def __str__(self):
		return self.map_title

class Location(models.Model):
	"""A Location on a map, that we can point to"""
	map = models.ForeignKey(Map, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	#x_coordinate = models.IntegerField(Map.map_image.height_field)
	#y_coordinate = models.IntegerField(Map.map_image.width_field)

	def __str__(self):
		return self.title