from django.urls import path
import turist
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

app_name = 'travel_agency'
urlpatterns = [
    path('', TemplateView.as_view(template_name='f.html'),name="f"),
    path('tours/', views.tours, name='tours'),
    path('f/', views.f, name='tours'),
    path('tours/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('hotels/', views.hotels, name='hotels'),
    path('hotels/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('cities/', views.cities, name='cities'),
    path('cities/<int:city_id>/', views.city_detail, name='city_detail'),
    path('places/', views.places, name='places'),
    path('places/<int:place_id>/', views.place_detail, name='place_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)