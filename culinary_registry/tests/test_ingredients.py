from django.test import Client
from model_bakery import baker, seq

from culinary_registry.models import Ingredient


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

    assert ingredient.calory == calories


def test_list_all_ingredients_without_ingredients(db):
    c = Client()

    request = c.get("/api/culinary/list/ingredients")
    response = request.json()

    assert request.status_code == 200
    assert len(response['ingredients']) == 0


def test_list_all_ingredients(db):
    c = Client()
    baker.make("Ingredient", _quantity=10)

    request = c.get("/api/culinary/list/ingredients")
    response = request.json()

    assert request.status_code == 200
    assert len(response['ingredients']) == 10


def test_list_all_ingredients_pagination(db):
    c = Client()
    baker.make("Ingredient", name=seq('ingredient'), _quantity=25)

    request_page1 = c.get("/api/culinary/list/ingredients?page=1")
    response_page1 = request_page1.json()

    assert request_page1.status_code == 200
    assert len(response_page1['ingredients']) == 15

    request_page2 = c.get("/api/culinary/list/ingredients?page=2")
    response_page2 = request_page2.json()
    
    assert request_page2.status_code == 200
    assert len(response_page2['ingredients']) == 10
    assert response_page1['ingredients'] != response_page2['ingredients']


def test_list_all_ingredients_filter_by_name(db):
    c = Client()
    baker.make("Ingredient", name='Farinha de Trigo', brand=seq('marca'), _quantity=5)
    baker.make("Ingredient", name="Farinha de Arroz", brand=seq('marca'), _quantity=5)

    request = c.get("/api/culinary/list/ingredients?name=Farinha de Trigo")
    response = request.json()

    assert request.status_code == 200
    assert len(response['ingredients']) == 5


def test_list_all_ingredients_filter_by_brand(db):
    c = Client()
    baker.make("Ingredient", name='Farinha de Trigo', brand='marca')
    baker.make("Ingredient", name="Farinha de Arroz", brand='marca')

    request = c.get("/api/culinary/list/ingredients?brand=marca")
    response = request.json()

    assert request.status_code == 200
    assert len(response['ingredients']) == 2


def test_list_all_ingredients_filter_by_name_brand(db):
    c = Client()
    baker.make("Ingredient", name='Farinha de Trigo', brand='marca')
    baker.make("Ingredient", name="Farinha de Arroz", brand='marca')

    request = c.get("/api/culinary/list/ingredients?name=Farinha de Trigo&?brand=marca")
    response = request.json()

    assert request.status_code == 200
    assert len(response['ingredients']) == 1
    assert response['ingredients'][0]['name'] == 'Farinha de Trigo'
    assert response['ingredients'][0]['brand'] == 'marca'


def test_add_new_ingredient(db):
    c = Client()
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
    request = c.post("/api/culinary/new/ingredient", new_ingredient, content_type="application/json")
    response = request.json()

    assert request.status_code == 201
    assert new_ingredient["name"] == response['ingredient']['name']
    assert new_ingredient["brand"] == response['ingredient']['brand']
    assert new_ingredient["amount"] == response['ingredient']['amount']
    assert new_ingredient["calory"] != response['ingredient']['calory']


def test_add_duplicated_ingredient(db):
    c = Client()
    # Using baker to create an ingredient with the brand "Marca".
    baker.make(
        "Ingredient",
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
    # Ingredient dict with the same information as the ingredient created previously.
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

    request = c.post("/api/culinary/new/ingredient", new_ingredient, content_type="application/json")
    response = request.json()

    assert request.status_code == 400
    assert response['error']


def test_trying_to_create_ingredient_malformated(db):
    c = Client()
    new_ingredient = {
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

    request = c.post("/api/culinary/new/ingredient", new_ingredient, content_type="application/json")
    response = request.json()

    assert request.status_code == 400
    assert response['error']


def test_delete_ingredient(db):
    c = Client()
    new_ingredient = baker.make("Ingredient", pk=1, name="Farinha de Trigo")
    
    ingredient = Ingredient.objects.filter(pk=new_ingredient.pk).exists()
    assert ingredient

    request = c.post("/api/culinary/delete/ingredient/1")
    response = request.json()

    ingredient = Ingredient.objects.filter(pk=new_ingredient.pk).exists()
    
    assert request.status_code == 200
    assert not ingredient
    assert response['deleted_ingredient']['name'] == new_ingredient.name


def test_delete_non_existent_ingredient(db):
    c = Client()

    request = c.post("/api/culinary/delete/ingredient/1")
    response = request.json()
    
    assert request.status_code == 404
    assert response['error'] == 'Ingrediente não encontrado'


def test_delete_right_ingredient(db):
    c = Client()

    baker.make("Ingredient", pk=1)
    baker.make("Ingredient", pk=2)
    ingredients = Ingredient.objects.all()

    assert len(ingredients) == 2

    request = c.post("/api/culinary/delete/ingredient/1")
    response = request.json()

    ingredient = Ingredient.objects.filter(pk=1).exists()
    ingredients = Ingredient.objects.all()

    assert request.status_code == 200
    assert not ingredient
    assert len(ingredients) == 1
    assert ingredients[0].id == 2
