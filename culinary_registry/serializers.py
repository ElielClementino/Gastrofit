class IngredientSerializer:
    @staticmethod
    def to_json(instance):
        return {
            'name': instance.name,
            'brand': instance.brand,
            'calory': instance.calory,
            'amount': instance.amount,
            'carbohydrate': instance.carbohydrate,
            'protein': instance.protein,
            'total_fat': instance.total_fat,
            'trans_fat': instance.trans_fat,
            'saturated_fat': instance.saturated_fat,
            'fiber': instance.fiber,
            'sodium': instance.sodium,
        }

    @staticmethod
    def to_json_list(queryset):
        return [IngredientSerializer.to_json(instance) for instance in queryset]
