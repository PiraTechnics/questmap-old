from django.urls import path
from . import views

app_name = 'maps'
urlpatterns = [
	# Home Page
	path('', views.index, name='index'),
	# Page to show links to all campaigns
	path('campaigns/', views.campaigns, name='campaigns'),
	# Path to show a single campaign
	path('campaigns/<int:camp_id>', views.campaign, name='campaign'),
	# Path for adding a new Campaign
	path('campaigns/new_campaign', views.new_campaign, name='new_campaign'),
	# Path for editing/deleting a Campaign
	path('campaigns/edit/<int:camp_id>', views.edit_campaign, name='edit_campaign'),	
	# Path for joining a Campaign as a Player
	path('campaigns/join/<int:camp_id>', views.join_campaign, name='join_campaign'),
	# Page to show links to all characters
	path('characters/', views.characters, name='characters'),
	# Page to show a single character's profile
	path('characters/<int:char_id>', views.character, name='character'),
	# Page for adding a new character
	path('characters/new_character', views.new_character, name='new_character'),
	# Page to show links to all maps
	path('maps/', views.maps, name = 'maps'),
	# Page to display a single map
	path('maps/<int:map_id>/', views.map, name='map'),
	# Page for adding a new map
	path('maps/new_map', views.new_map, name='new_map'),
	# Page to display a single location, and all notes about it
	# Also includes a form to add new notes
	path('locations/<int:location_id>/', views.location, name='location'),
	# Page for adding a new location
	path('maps/<int:map_id>/new_location', views.new_location, name='new_location'),
]