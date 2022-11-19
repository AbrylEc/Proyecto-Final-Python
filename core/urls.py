from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('biography/', views.biography, name="biography"),
    path('gallery/', views.gallery, name="gallery"),
]
