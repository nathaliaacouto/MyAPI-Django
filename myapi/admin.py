from django.contrib import admin
from myapi.models import User

class Users(admin.ModelAdmin):
        list_display = ('id', 'nome', 'email')
        list_display_links = ('id', 'email')
        search_fields = ('email',)

admin.site.register(User, Users)