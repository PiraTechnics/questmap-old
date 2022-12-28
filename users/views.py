from django.shortcuts import render, redirect
from django.core import exceptions
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import UserCreationForm

def register(request):
	"""Register a new user"""
	if request.method != 'POST':
		# Display blank registration form
		form = UserCreationForm()
	else:
		# Process completed registration form
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			
			# Default add as a player
			group = Group.objects.get(name='Players')
			new_user.groups.add(group)
			
			# Now log the user in, and redirect to home page
			login(request, new_user)
			return redirect('maps:index')

	# Display blank or invalid form
	context = {'form': form}
	return render(request, 'registration/register.html', context)

@login_required
def profile(request, username):
	"""Display User Info"""
	user = User.objects.get(username=username)

	if request.user != user:
		# This isn't the current user's profile -- forbidden
		raise exceptions.PermissionDenied
	else:
		groups = user.groups.all()
		context = {'user': user, 'groups': groups}
		return render(request, 'users/profile.html', context)

#def edit_profile(request, username):
	"""Edit our user info"""

