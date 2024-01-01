import json

from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from pydantic import ValidationError

from culinary_registry.forms import ingredient_form
from culinary_registry.service import ingredient_svc


@require_GET
def list_ingredients(request):
    page_number = request.GET.get('page', 1)
    params = request.GET

    try:
        ingredient_service_result = ingredient_svc.list_ingredients(params)

        paginator = Paginator(ingredient_service_result, 15)
        ingredients_page = paginator.page(page_number).object_list

        return JsonResponse({"ingredients": ingredients_page, "page": page_number, "total_pages": paginator.num_pages})

    except Exception as e:
        return JsonResponse({"error": f"Erro inesperado: {e}"}, status=500)


@require_POST
def add_ingredient(request):
    try:
        ingredient_data = json.loads(request.body.decode())

        ingredient_form.IngredientForm(**ingredient_data)

        ingredient_service_result = ingredient_svc.add_ingredient(ingredient_data)

        return JsonResponse({"ingredient": model_to_dict(ingredient_service_result)}, status=201)

    except ValueError as ve:
        return JsonResponse({"error": f"Erro de análise JSON: {ve}"}, status=400)

    except ValidationError as ife:
        return JsonResponse({"error": f"Dados do formulário inválidos: {ife}"}, status=400)

    except Exception as e:
        return JsonResponse({"error": f"Erro inesperado: {e}"}, status=500)
