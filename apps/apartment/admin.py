from django.contrib import admin
from apps.apartment import models

# Register your models here.

class CategoryFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)

################################################################################################################################################################################

class FloorFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)


################################################################################################################################################################################

class RoomsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)

################################################################################################################################################################################

class StatusFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)

################################################################################################################################################################################

class ApartmentInline(admin.TabularInline):
    model = models.ApartmentOsob
    extra = 1

class ApartmentFilterAdmin(admin.ModelAdmin):
    list_filter = ('room',)
    list_display = ('room',)
    search_fields = ('room',)
    inlines = [ApartmentInline]

################################################################################################################################################################################

admin.site.register(models.Rooms,RoomsFilterAdmin)
admin.site.register(models.Category,CategoryFilterAdmin)
admin.site.register(models.Status,StatusFilterAdmin)
admin.site.register(models.Apartment,ApartmentFilterAdmin)
admin.site.register(models.Floor,FloorFilterAdmin)

