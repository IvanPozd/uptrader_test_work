from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu_item_detail, name='menu_item_detail'),
    path('person_area', views.menu_item_detail),
    path('profile', views.menu_item_detail),
    path('contacts', views.menu_item_detail),
    path('sports', views.menu_item_detail),
    path('basketball', views.menu_item_detail),
    path('football', views.menu_item_detail),
]
