"""turizm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
## project/urls.py
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('turist.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# path('login/', views.user_login, name='login'),
# path('login/', views.login_view, name='login'),
# path('logout/', views.user_logout, name='logout'),
# path('register/', views.user_register, name='register'),
#path('users/<int:user_id>/', views.user_detail, name='user_detail'),
#path('tours/<int:tour_id>/', views.tour_detail, name='tour_detail'),
#path('tours/<int:tour_id>/add_comment/', views.add_comment, name='add_comment'),
# path('admin/', admin.site.urls),

