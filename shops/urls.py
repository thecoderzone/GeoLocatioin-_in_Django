from django.urls import path
from . import views

urlpatterns = [
    path('shops/', views.find_shops, name='find_shops'),
]