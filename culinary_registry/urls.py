from django.urls import path
from . import views


urlpatterns = [
    path('new/ingredient', views.add_ingredient),
]
