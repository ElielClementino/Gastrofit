from django.http import JsonResponse
from django.forms.models import model_to_dict
from culinary_registry.forms import ingredient_form
from culinary_registry.service import ingredient_svc
from django.views.decorators.http import require_POST
from pydantic import ValidationError
import json


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

