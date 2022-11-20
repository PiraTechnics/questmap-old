from django import forms
from .models import Map

class MapForm(forms.modelForm):
	class Meta:
		model = Map
		fields = ['map_title', 'map_image']