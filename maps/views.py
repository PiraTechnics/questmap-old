from django.shortcuts import render
from .models import Map

def index(request):
	# We will want to display only a single map, should be only one for now
	data = Map.objects.all()
	first_map = data.get(id=1)

	context = {'data' : data}
	return render(request, "maps/display.html", context)