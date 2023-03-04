from django.urls import path
from . import views

app_name = 'travel_agency'
urlpatterns = [
    path('', views.index, name='index'),
    path('tours/', views.tours, name='tours'),
    path('tours/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('hotels/', views.hotels, name='hotels'),
    path('hotels/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('cities/', views.cities, name='cities'),
    path('cities/<int:city_id>/', views.city_detail, name='city_detail'),
    path('places/', views.places, name='places'),
    path('places/<int:place_id>/', views.place_detail, name='place_detail'),
]
