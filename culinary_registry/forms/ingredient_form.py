from pydantic import BaseModel


class IngredientForm(BaseModel):
    name: str
    brand: str
    amount: float
    carbohydrate: float
    protein: float
    total_fat: float
    trans_fat: float
    saturated_fat: float
    fiber: float
    sodium: float
    calory: float = 0
