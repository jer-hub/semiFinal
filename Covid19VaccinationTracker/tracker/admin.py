from django.contrib import admin
from .models import Person,Vaccine

admin.site.site_header = 'Covid19 - Vaccination Tracker Admin'
admin.site.site_title = 'Covid19 - Vaccination Tracker Admin Area'
admin.site.index_title = 'Welcome to  Covid19 - Vaccination Tracker Admin Area'

# Register your models here.
class Vaccined(admin.ModelAdmin):
    list_display = ('lastName', 'firstName', 'contact','brgy','street','houseno','city','vaccine')


admin.site.register(Person, Vaccined)
admin.site.register(Vaccine)