from django import forms
from .models import Map

class MapForm(forms.ModelForm):
	class Meta:
		model = Map
		fields = ['map_title', 'map_image']
		labels = {'map_title': 'Name', 'map_image': 'Image'}