from django.contrib import admin
from .models import Chat, Lesson, UserProfile, Messages

admin.site.register(Chat)
admin.site.register(Lesson)
admin.site.register(UserProfile)
admin.site.register(Messages)
