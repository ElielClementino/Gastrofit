from django.db.models import Q

from culinary_registry.models import Ingredient
from culinary_registry.serializers import IngredientSerializer


def list_ingredients(params):
    ingredients = Ingredient.objects.all()

    if 'name' in params:
        ingredients = ingredients.filter(name=params['name'])
    if 'brand' in params:
        ingredients = ingredients.filter(brand=params['brand'])
    if 'name' in params and 'brand' in params:
        ingredients = ingredients.filter(Q(name=params['name']) & Q(brand=params['brand']))

    serialized_data = IngredientSerializer.to_json_list(ingredients)

    return serialized_data


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


def delete_ingredient(ingredient_id):
    ingredient = Ingredient.objects.get(pk=ingredient_id)

    ingredient.delete()

    return ingredient


def update_ingredient(updated_ingredient, pk):

    Ingredient.objects.filter(pk=pk).update(**updated_ingredient)

    updated_ingredient = Ingredient.objects.get(pk=pk)

    return updated_ingredient
