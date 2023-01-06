from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	return render(request, "maps/index.html")

"""
def add(request):
	if request.method == 'POST':
		# POST data submitted -- process it
		form = ModelForm(request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			# Now set all the variables relevants...
			new_entry.user = request.user
	else:
		# Render Blank or invalid form

Come back to this later..."""
