from django.contrib import admin
from .models import Note, Image

admin.site.register(Note)

class imageAdmin(admin.ModelAdmin):
	list_display = ["title", "photo"]

admin.site.register(Image, imageAdmin)