from django.db import models

class Map(models.Model):
	"""A Map that we can view on a page and interact with"""
	map_title = models.CharField(max_length=50)
	map_image = models.ImageField(upload_to='upload/')