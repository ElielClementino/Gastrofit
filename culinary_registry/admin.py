from django.contrib import admin

from culinary_registry.models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('name', 'brand',)
    ordering = ('name',)
