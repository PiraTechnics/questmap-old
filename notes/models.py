from django.db import models

class Note(models.Model):
	"""A note on any topic
	This will evnetually be tied to a set of coordinates on a specific map
	and will be owned by a user, and have toggable visibility.

	For now though, let's keep things simple"""
	# Do we even need a title? Probably not right now...
	#title = models.Charfield(max_length=200)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return a string rep of the model"""
		return self.text

class Image(models.Model):
	title = models.CharField(max_length=20)
	photo = models.ImageField(upload_to='images')