from django.contrib import admin
from apps.contacts import models
# Register your models here.

class ContactFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

################################################################################################################################################################################

class ContactInfoFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

################################################################################################################################################################################

admin.site.register(models.ContactInfo, ContactInfoFilterAdmin)
admin.site.register(models.Contact, ContactFilterAdmin)
