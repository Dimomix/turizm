#turist.urls.py
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import Register
# app_name = 'turist'
urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'),name='home'),
    path('asda/',TemplateView.as_view(template_name='f.html'),name='asda'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/register/',Register.as_view(),name='register'),
    path('tours/', views.tours, name='tours'), 
    path('asd/',views.asd, name='asd'),
    path('f/', views.f, name='ftours_as'),
    path('tours/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('hotels/', views.hotels, name='hotels'),
    path('hotels/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('cities/', views.cities, name='cities'),
    path('cities/<int:city_id>/', views.city_detail, name='city_detail'),
    path('places/', views.places, name='places'),
    path('places/<int:place_id>/', views.place_detail, name='place_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)