from django.contrib import admin
from .models import CustomUser, Service, GalleryItem, Expert, Partner, Reservation

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ['title', 'description']

class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']

class ExpertAdmin(admin.ModelAdmin):
    list_display = ('name', 'expertise')
    search_fields = ['name', 'expertise']

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

admin.site.register(CustomUser)
admin.site.register(Service, ServiceAdmin)
admin.site.register(GalleryItem, GalleryItemAdmin)
admin.site.register(Expert, ExpertAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Reservation)

# Personnalisation de l'interface d'administration
admin.site.site_header = "Administration ACKIM PRO"
admin.site.site_title = "ACKIM PRO Admin Portal"
admin.site.index_title = "Bienvenue dans l'administration ACKIM PRO"
