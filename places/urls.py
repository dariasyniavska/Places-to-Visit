from django.urls import path

from places import views

urlpatterns = [
    path('', views.index, name='index'),
    path('places/', views.place_list, name='place_list'),
    path('places/add/', views.add_place, name='add_place'),
    path('places/<int:place_id>/', views.place_detail, name='place_detail'),
]
