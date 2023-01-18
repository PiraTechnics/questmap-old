from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from maps.models import Campaign, Map
from maps.forms import MapForm

# All views for Map

@login_required
@permission_required('maps.view_map', raise_exception=True)
def maps(request):
	"""Show all the maps as a list of links"""
	maps = Map.objects.filter(user=request.user).order_by('title')
	context = {'maps': maps}
	return render(request, 'maps/maps.html', context)

@login_required
@permission_required('maps.view_map', raise_exception=True)
def map(request, map_id):
	"""Show a single map"""
	map = Map.objects.get(id=map_id)
	locations = map.location_set.order_by('title')
	context = {'map': map, 'locations': list(locations.values())}
	return render(request, 'maps/map.html', context)

@login_required
@permission_required('maps.add_map', raise_exception=True)
def new_map(request):
	"""Add a new map"""
	if request.method != 'POST':
		# No data submitted -- create blank form
		form = MapForm()
		# Only allow GM to add a map to a campaign they own
		form.fields['campaign'].queryset = Campaign.objects.filter(user=request.user)
	else:
		# POST data submitted -- process it
		form = MapForm(request.POST, request.FILES)
		if form.is_valid():
			new_map = form.save(commit=False)
			new_map.user = request.user
			new_map.save()
			map_obj = form.instance
			return render(request, 'maps/new_map.html', {'form': form, 'map_obj': map_obj})

	# Display a blank or invalid form
	context = {'form': form}
	return render(request, 'maps/new_map.html', context)