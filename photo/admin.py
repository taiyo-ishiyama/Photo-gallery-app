from django.contrib import admin

# Register your models here.
from .models import Category, PhotoPost

class CategoryAdmin(admin.ModelAdmin):
  # display id and title
  list_display = ('id', 'title')
  # Link url
  list_display_links = ('id', 'title')

class PhotoPostAdmin(admin.ModelAdmin):
  # display id and title
  list_display = ('id', 'title')
  # link url
  list_display_links = ('id', 'title')

# register category and categoryadmin for django management
admin.site.register(Category, CategoryAdmin)

# register PhotoPost and PhotoPostAdmin for django management
admin.site.register(PhotoPost, PhotoPostAdmin)

