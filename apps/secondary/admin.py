from django.contrib import admin

from apps.secondary import models

# Register your models here.


class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)

class ProjectsFilterAdmin(admin.ModelAdmin):
    list_filter = ('image', )
    list_display = ('image',)
    search_fields = ('image',)

admin.site.register(models.Slide, SlideFilterAdmin)
admin.site.register(models.Projects, ProjectsFilterAdmin)
