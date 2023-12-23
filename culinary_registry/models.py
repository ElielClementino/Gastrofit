from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    brand = models.CharField(max_length=120, blank=True)
    amount = models.FloatField()
    carbohydrate = models.FloatField()
    protein = models.FloatField()
    total_fat = models.FloatField()
    trans_fat = models.FloatField()
    saturated_fat = models.FloatField()
    fiber = models.FloatField()
    sodium = models.FloatField()
    calory = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
