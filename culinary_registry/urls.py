from django.urls import path

from . import views

urlpatterns = [
    path('list/ingredients/', views.list_ingredients),
    path('new/ingredient/', views.add_ingredient),
    path('delete/ingredient/<int:pk>/', views.delete_ingredient),
    path('update/ingredient/<int:pk>/', views.update_ingredient),
]
