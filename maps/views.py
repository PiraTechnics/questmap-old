from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Campaign, Character, Map, Location
from .forms import CampaignForm, CharacterForm, MapForm, LocationForm, NoteForm

@login_required
def index(request):
	return render(request, "maps/index.html")

@login_required
def campaigns(request):
	"""Show all of the user's campaigns"""
	#Note: this will intially ownly apply to the owner of a campaign
	#We will add functionality for players to see their campaigns after
	user = request.user
	campaigns = Campaign.objects.filter(user=user)
	context = {'campaigns': campaigns}
	return render(request, 'maps/campaigns.html', context)

@login_required
def campaign(request, camp_id):
	"""Show a single campaign"""
	user = request.user
	campaign = Campaign.objects.get(id=camp_id)
	characters = Character.objects.filter(campaign=camp_id)
	maps = Map.objects.filter(campaign=camp_id)
	context = {'campaign': campaign, 'characters': characters, 'maps': maps}
	return render(request, 'maps/campaign.html', context)

@login_required
def new_campaign(request):
	"""Add a new Campaign -- GMs only"""
	if request.method != 'POST':
		# No data submitted - create blank for
		form = CampaignForm()
	else:
		# POST data submitted - process it
		form = CampaignForm(request.POST)
		if form.is_valid():
			new_camp = form.save(commit=False)
			new_camp.user = request.user
			new_camp.save()
			return redirect('maps:campaigns')

	# Display a blank or invalid form
	context = {'form': form}
	return render(request, 'maps/new_campaign.html', context)

@login_required
def characters(request):
	"""Shows all of a user's characters"""
	characters = Character.objects.filter(user=request.user).order_by('char_name') # Limit to the current user's characters
	# NOTE: Will need to find a way to limit url inputs to stop users from seeing characters they don't own...unless we want to allow that in some cases?
	context = {'characters': characters}
	return render(request, 'maps/characters.html', context)

@login_required
def character(request, char_id):
	"""Show a single character's profile"""
	character = Character.objects.get(id=char_id)
	context = {'character': character}
	return render(request, 'maps/character.html', context)

@login_required
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

@login_required
def maps(request):
	"""Show all the maps as a list of links"""
	maps = Map.objects.order_by('map_title')
	context = {'maps': maps}
	return render(request, 'maps/maps.html', context)

@login_required
def map(request, map_id):
	"""Show a single map"""
	map = Map.objects.get(id=map_id)
	locations = map.location_set.order_by('title')
	context = {'map': map, 'locations': locations}
	return render(request, 'maps/map.html', context)

@login_required
def new_map(request):
	"""Add a new map"""
	if request.method != 'POST':
		# No data submitted -- create blank form
		form = MapForm()
	else:
		# POST data submitted -- process it
		form = MapForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			map_obj = form.instance
			return render(request, 'maps/new_map.html', {'form': form, 'map_obj': map_obj})

	# Display a blank or invalid form
	context = {'form': form}
	return render(request, 'maps/new_map.html', context)

@login_required
def location(request, location_id):
	"""Show a specific location for a map, and all its associated notes"""
	location = Location.objects.get(id=location_id)
	notes = location.note_set.order_by('-created')

	# Include form to add a new note to the location
	if request.method != 'POST':
		# Blank form by default
		form = NoteForm()
		# Only allow choice of author to be one of the current user's characters
		form.fields['author'].queryset = Character.objects.filter(user=request.user)

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
			new_location.map = map
			new_location.save()
			return redirect('maps:map', map_id=map_id)

	# Display blank or invalid form
	context = {'map': map, 'form': form}
	return render(request, 'maps/new_location.html', context)