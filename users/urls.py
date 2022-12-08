"""Defines Django Patterns for users of QuestMap"""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
	# Include default auth urls
	path('', include('django.contrib.auth.urls')),
	# Registration Page
	path('register/', views.register, name='register'),
]