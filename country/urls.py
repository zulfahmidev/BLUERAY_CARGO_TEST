from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='country.index'),
    path('create', views.create, name='country.create'),
    path('edit/<int:country_id>', views.edit, name='country.edit'),
    path('delete/<int:country_id>', views.delete, name='country.delete'),
]