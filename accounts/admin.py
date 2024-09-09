from django.contrib import admin

# Register your models here.

from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
  # cnofigure column for the admin page

  # display id and username for record list
  list_display=('id', 'username')

  # Configure the link for column
  list_display_links=('id', 'username')

# Register CustomUser and CustomUserAdmin for Django admin page
admin.site.register(CustomUser, CustomUserAdmin)