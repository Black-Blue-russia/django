from django.urls import path
from .import views

urlpatterns=[
    path('', views.home, name='home'),
    path('building1/', views.building1, name="building1"),
    path('building2/', views.building2, name="building2"),
    path('building3/', views.building3, name="building3"),
    path('map/', views.map, name="map"),
]