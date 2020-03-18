from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Categories

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author


class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)
    resource_class = CategoryResource

class AuthorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['names', 'last_names','email']
    list_display = ('names','last_names', 'email')
    resource_class = Author

admin.site.register(Author, AuthorAdmin)
admin.site.register(Categories,CategoryAdmin)
admin.site.register(Post)