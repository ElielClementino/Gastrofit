from model_bakery import baker
from culinary_registry.models import Recipe, RecipeIngredient, Ingredient


def calculate_calories(obj):
     """
     Logic being used on model to calculate automatically the calories of an ingredient, when
     created, based on it's macros.
     """
        carbohydrate_calories = obj.carbohydrate * 4
        protein_calories = obj.protein * 4
        total_fat_calories = obj.total_fat * 9
        trans_fat_calories = obj.trans_fat * 9
        saturated_fat_calories = obj.saturated_fat * 9
        fiber_calories = obj.fiber * 4
        calories = carbohydrate_calories + protein_calories + total_fat_calories + trans_fat_calories + saturated_fat_calories + fiber_calories
        
        return calories

def test_if_calories_is_being_calculated_correctly(db):
    Ingredient.objects.create(
        name = "Farinha de Trigo",
        brand = "Marca",
        amount = 100,
        carbohydrate = 15.02,
        protein = 1.96,
        total_fat = 0.28,
        trans_fat = 0,
        saturated_fat = 0.04,
        fiber = 0.46,
        sodium = 0.20,
    )

    ingredient = Ingredient.objects.first()

    calories = calculate_calories(ingredient)

    assert ingredient.calories == calories


def test_add_new_ingredient(client, db):

    new_ingredient = {
        "name": "Farinha de Trigo",
        "brand": "Marca",
        "amount": 100,
        "carbohydrate": 15.02,
        "protein": 1.96,
        "total_fat": 0.28,
        "trans_fat": 0,
        "saturated_fat": 0.04,
        "fiber": 0.46,
        "sodium": 0.20,
        "calory": 0,
    }
    request = client.post("api/culinary/new/ingredient", new_ingredient, content_type="application/json")

    response = request.json()

    assert request.status_code = 201
    assert new_ingredient["name"] == response.name
    assert new_ingredient["brand"] == response.brand
    assert new_ingredient["amount"] == response.amount
    assert new_ingredient["calory"] != response.calory
