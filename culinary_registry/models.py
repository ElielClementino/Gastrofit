from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=120)
    brand = models.CharField(max_length=120, blank=True)
    amount = models.FloatField(default=0)
    carbohydrate = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    total_fat = models.FloatField(default=0)
    trans_fat = models.FloatField(default=0)
    saturated_fat = models.FloatField(default=0)
    fiber = models.FloatField(default=0)
    sodium = models.FloatField(default=0)
    calory = models.FloatField(blank=True, null=True)

    def calculate_calories(self):
        carbohydrate_calories = self.carbohydrate * 4
        protein_calories = self.protein * 4
        total_fat_calories = self.total_fat * 9
        trans_fat_calories = self.trans_fat * 9
        saturated_fat_calories = self.saturated_fat * 9
        fiber_calories = self.fiber * 4
        calories = carbohydrate_calories + protein_calories + total_fat_calories + trans_fat_calories + saturated_fat_calories + fiber_calories

        return calories

    def __str__(self):
        return self.name


@receiver(post_save, sender=Ingredient)
def calculate_calories_on_save(sender, instance, **kwargs):
    if instance.calory is None:
        instance.calory = instance.calculate_calories()
        instance.save()


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    total_carbohydrate = models.FloatField(default=0)
    total_protein = models.FloatField(default=0)
    total_total_fat = models.FloatField(default=0)
    total_trans_fat = models.FloatField(default=0)
    total_saturated_fat = models.FloatField(default=0)
    total_fiber = models.FloatField(default=0)
    total_sodium = models.FloatField(default=0)
    total_calory = models.FloatField(default=0)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField()
