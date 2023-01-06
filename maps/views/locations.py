from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

from maps.models import Character, Map, Location
from maps.forms import LocationForm, NoteForm

# All view for Location

@login_required
@permission_required('maps.view_location', raise_exception=True)
def location(request, location_id):
	"""Show a specific location for a map, and all its associated notes"""
	location = Location.objects.get(id=location_id)
	notes = location.note_set.order_by('-created')

	# Include form to add a new note to the location
	if request.method != 'POST':
		# Blank form by default
		form = NoteForm()
		# Only allow choice of author to be one of the current user's characters, and that they are a part of the campaign
		form.fields['author'].queryset = Character.objects.filter(user=request.user).filter(campaign=location.map.campaign)

	else:
		# Submit the POST data and process it
		form = NoteForm(data=request.POST)
		if form.is_valid():
			new_note = form.save(commit=False)
			new_note.user = request.user
			new_note.location = location
			new_note.save()
			return redirect('maps:location', location_id=location_id)

	# Render page with all notes and an empty form for submitting a new note
	context = {'location': location, 'notes': notes, 'form': form}
	return render(request, 'maps/location.html', context)

@login_required
@permission_required('maps.add_location', raise_exception=True)
def new_location(request, map_id):
	"""Add a new location for a given map"""
	map = Map.objects.get(id=map_id)
	xCoord = request.GET.get('xCoord', '')
	yCoord = request.GET.get('yCoord', '')

	if request.method != 'POST':
		# No data submitted -- create blank form
		# BUT make sure to add in the coordinates from URL params
		form = LocationForm(initial={'xCoord': xCoord, 'yCoord': yCoord})
	else:
		# POST data submitted -- process it
		form = LocationForm(data=request.POST)
		if form.is_valid():
			new_location = form.save(commit=False)
			new_location.user = request.user
			new_location.map = map
			new_location.save()
			return redirect('maps:map', map_id=map_id)

	# Display blank or invalid form
	context = {'map': map, 'form': form}
	return render(request, 'maps/new_location.html', context)