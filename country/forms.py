from django import forms
from .models import Country

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country_name', 'country_flag', 'country_currency']