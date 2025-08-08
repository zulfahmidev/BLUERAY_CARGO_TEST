from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='category.index'),
    path('create', views.create, name='category.create'),
    path('edit/<int:category_id>', views.edit, name='category.edit'),
    path('delete/<int:category_id>', views.delete, name='category.delete'),

    path('api/categories', views.api_index),
]