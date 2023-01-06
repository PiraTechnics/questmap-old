from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied, BadRequest
from django.contrib import messages

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
	if check_campaign_access(request.user, campaign):
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
	
	if request.method != 'POST':
		form = JoinCampaignForm()
		# Only allow choice of character to be one of the user's current characters, that has no campaign
		form.fields['character'].choices = Character.objects.filter(user=request.user).filter(campaign=None)
		# This doesn't seem to work, we don't populate the field...
	else:
		# POST data submitted - process it
		form = JoinCampaignForm(request.POST)
		if form.is_valid():
			#character = form.cleaned_data['character']
			#pc_entry = Character.objects.get(char_name=character)
			#pc_entry.campaign = campaign
			#not failing, but this doesn't appear to do anything...
			form.save()
			return render_campaign(request, campaign)

	# Display a blank or invalid form
	context = {'form': form, 'campaign': campaign}
	return render(request, 'maps/join_campaign.html', context) # BUG: IF user has no characters and submits anyway, they get access to all the characters
	# need to filter on this as well -- invalid form behavior


"""Verify an invite from GM, then allow user to join the specific campaign
How to do this? A unique token? a prefilled form? etc etc"""

""" -- WIP
@login_required
@permission_required('maps.change_campaign', 'maps.delete_campaign', raise_exception=True)
def edit_campaign(request, camp_id):
	#Allow a GM to edit their own Campaign
	campaign = Campaign.objects.get(id=camp_id)
	# Ensure user is the campaign's owner
	if request.user != campaign.user:
		# Give us a permission denied
		raise PermissionDenied
	else: # user validated -- let them edit it
		characters = Character.objects.filter(campaign=camp_id)
		maps = Map.objects.filter(campaign=camp_id)
		context = {'campaign': campaign, 'characters': characters, 'maps': maps}
		return render(request, 'maps/edit_campaign.html', context)
"""

# Helper Functions

def check_campaign_access(user, campaign):
	is_player = False
	is_gm = False
	characters = Character.objects.filter(campaign=campaign.id)
	# Check if user has a character in campaign
	for char in characters:
		if user == char.user:
			is_player = True
			break
	# Check if user is owner of campaign
	if user == campaign.user:
		is_gm = True

	return is_player or is_gm

def render_campaign(request, campaign):
		characters = Character.objects.filter(campaign=campaign.id)
		maps = Map.objects.filter(campaign=campaign.id)
		context = {'campaign': campaign, 'characters': characters, 'maps': maps}
		return render(request, 'maps/campaign.html', context)