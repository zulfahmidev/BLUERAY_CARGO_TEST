from django.contrib import admin
from .models import Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ('coountry_name', 'coountry_flag', 'coountry_currency')  # kolom yang ditampilkan di tabel admin
    search_fields = ('coountry_name',)

admin.site.register(Country)
