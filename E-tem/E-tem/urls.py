from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('allauth/', include('allauth.urls')),
    path('login/', include('login.urls')),
]
