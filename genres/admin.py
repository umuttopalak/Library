from django.contrib import admin

from .models import Genre


# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]
    
admin.site.register(Genre , GenreAdmin)