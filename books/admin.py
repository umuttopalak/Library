from django.contrib import admin

from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):

    list_display = ('name' ,'genre' , 'author' ,)
    list_filter = ('genre' , 'author' ,)
    search_fields = ['name',]
    
admin.site.register(Book , BookAdmin)