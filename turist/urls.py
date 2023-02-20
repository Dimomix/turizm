from django.urls import path
from . import views

app_name = 'travel_agency'

urlpatterns = [
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('tours/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('tours/<int:tour_id>/add_comment/', views.add_comment, name='add_comment'),
]
