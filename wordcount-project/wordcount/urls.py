
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('count/', views.count, name='count'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('admin/', admin.site.urls),
]
