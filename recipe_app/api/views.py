from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from recipe_app.models import Recipe, Category, Ingredient
import json

class RecipeAPIView(View):
    def get(self, request, recipe_id=None):
        if recipe_id:
            try:
                recipe = Recipe.objects.get(pk=recipe_id)
                data = {
                    'id': recipe.id,
                    'title': recipe.title,
                    'description': recipe.description,
                    'cooking_steps': recipe.cooking_steps,
                    'cooking_time': recipe.cooking_time,
                    'author': recipe.author.username,
                }
                return JsonResponse(data)
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'Recipe not found'}, status=404)
        else:
            recipes = Recipe.objects.all()[:10]  # Limit to 10 for demo
            data = [{
                'id': r.id,
                'title': r.title,
                'author': r.author.username
            } for r in recipes]
            return JsonResponse({'recipes': data})