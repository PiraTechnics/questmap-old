from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied

from maps.models import Campaign, Character, Map
from maps.forms import CampaignForm, JoinCampaignForm

# All views for Campaign

@login_required
@permission_required("maps.view_campaign", raise_exception=True)
def campaigns(request):
	"""Show all of the user's campaigns"""
	#Note: this will intially ownly apply to the owner of a campaign
	#We will add functionality for players to see their campaigns after
	campaigns = Campaign.objects.filter(user=request.user)
	context = {'campaigns': campaigns}
	return render(request, 'maps/campaigns.html', context)

@login_required
@permission_required("maps.view_campaign", raise_exception=True)
def campaign(request, camp_id):
	"""Show a single campaign"""
	campaign = Campaign.objects.get(id=camp_id)
	if is_campaign_owner(request.user, campaign) or is_campaign_player(request.user, campaign):
		return render_campaign(request, campaign)
	else:
		raise PermissionDenied

@login_required
@permission_required("maps.add_campaign", raise_exception=True)
def new_campaign(request):
	"""Add a new Campaign -- GMs only"""
	if request.method != 'POST':
		# No data submitted - create blank form
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
@permission_required('maps.view_character', 'maps.change_character', raise_exception=True)
def join_campaign(request, camp_id):
	campaign = Campaign.objects.get(id=camp_id)
	char_names = Character.objects.values_list('id', 'name').filter(user=request.user).filter(campaign=None)
	
	if request.method != 'POST':
		form = JoinCampaignForm()
		# Only allow choice of character to be one of the user's current characters, that has no campaign
		form.fields['character'].choices = char_names
	else:
		# POST data submitted - process it
		form = JoinCampaignForm(request.POST)
		if form.is_valid():
			character = form.cleaned_data['character']
			pc_entry = Character.objects.get(id=character)
			pc_entry.campaign = campaign
			pc_entry.save()
			return render_campaign(request, campaign)

	# Display a blank or invalid form
	form.fields['character'].choices = char_names # clean up this code -- calling this twice but should redesign order to only need once
	context = {'form': form, 'campaign': campaign}
	return render(request, 'maps/join_campaign.html', context)


"""Verify an invite from GM, then allow user to join the specific campaign
How to do this? A unique token? a prefilled form? etc etc"""

@login_required
@permission_required('maps.change_campaign', 'maps.delete_campaign', raise_exception=True)
def edit_campaign(request, camp_id):
	#Allow a GM to edit their own Campaign
	campaign = Campaign.objects.get(id=camp_id)
	campaign_obj = get_object_or_404(Campaign, id=camp_id)
	# Ensure user is the campaign's owner
	if is_campaign_owner(request.user, campaign):
		form = CampaignForm(request.POST or None, instance=campaign_obj)
		
		if 'update' in request.POST:
			# update/edit campaign with changes
			if form.is_valid():
				form.save()
				return render_campaign(request, campaign_obj)
			else:
				# Serve Blank or invalid form
				context = {'form': form, 'campaign': campaign}
				return render(request, "maps/edit_campaign.html", context)
		elif 'delete' in request.POST:
			# Delete campaign
			campaign_obj.delete()
			return redirect('maps:campaigns')
		else:
			# Serve Blank or invalid form
			context = {'form': form, 'campaign': campaign}
			return render(request, "maps/edit_campaign.html", context)
	else:
		# Give us a permission denied
		raise PermissionDenied


# Helper Functions

def is_campaign_player(user, campaign):
	characters = Character.objects.filter(campaign=campaign.id)
	for char in characters:
		if user == char.user:
			return True
	
	# If we didnt find a character belonging to user in campaign, not a player
	return False

def is_campaign_owner(user, campaign):
	return user == campaign.user

def render_campaign(request, campaign):
		characters = Character.objects.filter(campaign=campaign.id)
		maps = Map.objects.filter(campaign=campaign.id)
		context = {'campaign': campaign, 'characters': characters, 'maps': maps}
		return render(request, 'maps/campaign.html', context)