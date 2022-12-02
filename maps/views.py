from django.shortcuts import render, redirect
from .models import Map, Location
from .forms import MapForm

def index(request):
	return render(request, "maps/index.html")

def maps(request):
	"""Show all the maps as a list of links"""
	maps = Map.objects.order_by('map_title')
	context = {'maps': maps}
	return render(request, 'maps/maps.html', context)

def map(request, map_id):
	"""Show a single map"""
	map = Map.objects.get(id=map_id)
	locations = map.location_set.order_by('title')
	context = {'map': map, 'locations': locations}
	return render(request, 'maps/map.html', context)

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


def location(request, location_id):
	"""Show a specific location for a map, and all its associated notes"""
	location = Location.objects.get(id=location_id)
	notes = location.note_set.order_by('-created')
	context = {'location': location, 'notes': notes}
	return render(request, 'maps/location.html', context)