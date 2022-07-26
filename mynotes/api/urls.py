# Create all the routes that the user can go to

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes')
]
