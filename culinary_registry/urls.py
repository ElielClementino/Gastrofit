from django.urls import path
from . import views


urlpatterns = [
    path('list/ingredients', views.list_ingredients),
    path('new/ingredient', views.add_ingredient),
]
