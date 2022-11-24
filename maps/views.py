from django.shortcuts import render
from .models import Map

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