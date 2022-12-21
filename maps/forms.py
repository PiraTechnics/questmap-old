from django import forms
from .models import Character, Map, Location, Note

class CharacterForm(forms.ModelForm):
	class Meta:
		model = Character
		fields = ['char_name']
		labels = {'char_name': 'Name'}

class MapForm(forms.ModelForm):
	class Meta:
		model = Map
		fields = ['map_title', 'map_image']
		labels = {'map_title': 'Name', 'map_image': 'Image'}

class LocationForm(forms.ModelForm):
	class Meta:
		model = Location
		fields = ['title', 'text', 'xCoord', 'yCoord']
		labels = {
			'title': 'Name',
			'text': 'Description',
			'xCoord': 'X Coordinate',
			'yCoord': 'Y Coordinate'
		}
		widgets = {'text': forms.Textarea(attrs={'cols': 80}),
			'xCoord': forms.HiddenInput(),
			'yCoord': forms.HiddenInput()
		}

class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['content', 'author']
		labels = {'content': '', 'author': 'Author'}
		widgets = {'content': forms.Textarea(attrs={'cols': 50, 'rows': 10})}