from django.urls import path
from . import views

app_name = 'maps'
urlpatterns = [
	# Home Page
	path('', views.index, name='index'),
	# Page to show links to all maps
	path('maps/', views.maps, name = 'maps'),
	# Page to show a single map
	path('maps/<int:map_id>/', views.map, name='map'),
	path('locations/<int:location_id>/', views.location, name='location'),
]