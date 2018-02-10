from django.db import models

# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'ingredients'


class Ratings(models.Model):
    rating = models.FloatField()
    createddate = models.DateTimeField()
    modifieddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ratings'


class Recipes(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=300)
    category = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    createddate = models.DateTimeField()
    instructions = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'recipes'


class RecipesIngredients(models.Model):
    id_recipes = models.ForeignKey(Recipes, models.DO_NOTHING, db_column='id_recipes', primary_key=True)
    id_ingredients = models.ForeignKey(Ingredients, models.DO_NOTHING, db_column='id_ingredients')

    class Meta:
        db_table = 'recipes_ingredients'
        unique_together = (('id_recipes', 'id_ingredients'),)


class RecipesRating(models.Model):
    id_recipe = models.ForeignKey(Recipes, models.DO_NOTHING, db_column='id_recipe', primary_key=True)
    id_ratings = models.ForeignKey(Ratings, models.DO_NOTHING, db_column='id_ratings')

    class Meta:
        db_table = 'recipes_rating'
        unique_together = (('id_recipe', 'id_ratings'),)