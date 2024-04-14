from django.contrib import admin

from channelapp.models import Room, Message

admin.site.register(Room)
admin.site.register(Message)