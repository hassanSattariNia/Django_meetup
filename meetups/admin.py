from django.contrib import admin

# Register your models here.
from .models import Meetup , Location , Participant

 
class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title','slug','location','date')
    list_filter = ('title','slug','date')
    prepopulated_fields={'slug':('title',)}
admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)