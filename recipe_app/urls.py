from django.urls import path
from . import views
from .views import RecipeDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add/', views.add_recipe, name='add_recipe'),
    path('recipe/edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('search/', views.search_recipes, name='search_recipes'),
]