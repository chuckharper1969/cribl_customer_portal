from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.destination_home),
    path('destination_home', views.destination_home, name="elastic_home"),
    path('destination_get/<int:pk>', views.destination_get, name="elastic_get"),
    path('destination_status/<int:pk>/<int:status>', views.destination_status, name="elastic_status"),
    path('destination_delete/<int:pk>', views.destination_delete, name="elastic_delete"),
    path('destination_update/<int:pk>', views.destination_update, name="elastic_update"),
    path('destination_add/', views.destination_add, name="elastic_add"),
]
