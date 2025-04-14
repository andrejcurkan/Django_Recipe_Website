from django.urls import path
from .views import RecipeAPIView

urlpatterns = [
    path('recipes/', RecipeAPIView.as_view(), name='api_recipes'),
    path('recipes/<int:recipe_id>/', RecipeAPIView.as_view(), name='api_recipe_detail'),
]