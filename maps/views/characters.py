from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

from maps.models import Character, Note
from maps.forms import CharacterForm

# All views for Character

@login_required
@permission_required('maps.view_character', raise_exception=True)
def characters(request):
	"""Shows all of a user's characters"""
	characters = Character.objects.filter(user=request.user).order_by('char_name') # Limit to the current user's characters
	context = {'characters': characters}
	return render(request, 'maps/characters.html', context)

@login_required
@permission_required('maps.view_character', raise_exception=True)
def character(request, char_id):
	"""Show a single character's profile"""
	#character = Character.objects.filter(user=request.user).get(id=char_id) #This shows a 'character doesn't exist' error if you click from the campaign
	character = Character.objects.get(id=char_id)
	notes = Note.objects.filter(author=character)
	context = {'character': character, 'notes': notes}
	return render(request, 'maps/character.html', context)

@login_required
@permission_required('maps.add_character', raise_exception=True)
def new_character(request):
	"""Add a new character"""
	if request.method != 'POST':
		# No data submitted - create blank form
		form = CharacterForm()
	else:
		# POST data submitted -- process it
		form = CharacterForm(request.POST)
		if form.is_valid():
			new_char = form.save(commit=False)
			new_char.user = request.user
			new_char.save()
			return redirect('maps:characters')
			
	# Display a blank or invalid form
	context = {'form': form}
	return render(request, 'maps/new_character.html', context)
