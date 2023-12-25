from django.contrib import admin
from django.contrib.auth.models import User,Group

#My imports 
from apps.base import models 

# Register your models here.
class SettingsPhoneInline(admin.TabularInline):
    model = models.SettingsPhone
    extra = 1  

class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    inlines = [SettingsPhoneInline]

################################################################################################################################################################################

class AboutFilterAdmin(admin.ModelAdmin):
    list_filter = ( 'descriptions', )
    list_display = ( 'descriptions', )
    search_fields = ( 'descriptions', )

################################################################################################################################################################################

class GalleryImageInline(admin.TabularInline):
    model = models.GalleryImage
    extra = 1

class GalleryFilterAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [GalleryImageInline]

################################################################################################################################################################################



################################################################################################################################################################################

admin.site.register(models.Settings, SettingsFilterAdmin)
admin.site.register(models.About, AboutFilterAdmin)
admin.site.register(models.Gallery, GalleryFilterAdmin)

################################################################################################################################################################################

admin.site.unregister(User)
admin.site.unregister(Group)
