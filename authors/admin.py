from django.contrib import admin

from .models import Author


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_filter = ('name', )

admin.site.register(Author , AuthorAdmin)
