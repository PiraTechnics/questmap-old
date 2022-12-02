from django.contrib import admin
from .models import Map, Location, Note

class mapAdmin(admin.ModelAdmin):
	list_display = ["map_title", "map_image"]

admin.site.register(Map, mapAdmin)
admin.site.register(Location)
admin.site.register(Note)
