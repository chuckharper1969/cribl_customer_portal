from django.urls import path
from . import views

urlpatterns = [
    path('elastic/get/', views.elastic_get),
    path('elastic/update/<int:pk>', views.elastic_update),
]
