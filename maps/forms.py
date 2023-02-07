from django import forms
from .models import Campaign, Character, Map, Location, Note

class CampaignForm(forms.ModelForm):
	class Meta:
		model = Campaign
		fields =['title', 'description']
		labels = {'title': 'Title', 'description': 'Summary'}

class CharacterForm(forms.ModelForm):
	class Meta:
		model = Character
		fields = ['name', 'description']
		labels = {'name': 'Name', 'description': 'Description'}

class MapForm(forms.ModelForm):
	class Meta:
		model = Map
		fields = ['title', 'image', 'campaign']
		labels = {'title': 'Name', 'image': 'Image', 'campaign': 'Campaign'}

class LocationForm(forms.ModelForm):
	class Meta:
		model = Location
		fields = ['title', 'size', 'type', 'text', 'xCoord', 'yCoord']
		labels = {
			'title': 'Name',
			'size': 'Size',
			'type': 'Type',
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

class JoinCampaignForm(forms.Form):
	# Note: Comment out this line and uncomment the following when setting up new env, then change back after migration
	character = forms.ChoiceField(choices=Character.objects.values_list('id', 'name'))
	# character = forms.CheckboxInput()