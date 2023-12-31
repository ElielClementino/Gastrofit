from django.db.models import Q
from culinary_registry.models import Ingredient


def add_ingredient(ingredient):
    if Ingredient.objects.filter(Q(name=ingredient['name']) & Q(brand=ingredient['brand'])).exists():
        raise ValueError('Este ingrediente dessa marca, já existe no banco de dados.')

    ingredient_dict = {
        'name': ingredient['name'],
        'brand': ingredient['brand'],
        'amount': ingredient['amount'],
        'carbohydrate': ingredient['carbohydrate'],
        'protein': ingredient['protein'],
        'total_fat': ingredient['total_fat'],
        'trans_fat': ingredient['trans_fat'],
        'saturated_fat': ingredient['saturated_fat'],
        'fiber': ingredient['fiber'],
        'sodium': ingredient['sodium'],
    }

    ingredient_obj = Ingredient.objects.create(**ingredient_dict)
    return ingredient_obj
