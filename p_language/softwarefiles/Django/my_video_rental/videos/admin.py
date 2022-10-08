from django.contrib import admin

# Register your models here.
from . import models

class MoviesAdmin(admin.ModelAdmin):
    #orderingField
    fields=['release_year','title','length']
    #Adding Search
    search_fields=['title']
    #Adding Filters
    list_filter=['release_year','length','title']
    #ADDING FIELDS
    list_display=['title','release_year','length']
    #EDITABLE LIST VIEW
    list_editable=['length']
admin.site.register(models.Customer)
admin.site.register(models.Movie,MoviesAdmin)
