from fastapi import APIRouter, HTTPException
from django.core.exceptions import ObjectDoesNotExist
from .models import Recipe, Category, Ingredient
from .schemas import RecipeSchema, CategorySchema, IngredientSchema

router = APIRouter()

@router.get("/recipes/", response_model=list[RecipeSchema])
async def get_all_recipes():
    recipes = Recipe.objects.all()
    return list(recipes)

@router.get("/recipes/{recipe_id}/", response_model=RecipeSchema)
async def get_recipe(recipe_id: int):
    try:
        return Recipe.objects.get(pk=recipe_id)
    except ObjectDoesNotExist:
        raise HTTPException(status_code=404, detail="Recipe not found")

@router.get("/recipes/search/title/{title}/", response_model=list[RecipeSchema])
async def search_recipes_by_title(title: str):
    recipes = Recipe.objects.filter(title__icontains=title)
    return list(recipes)

@router.get("/recipes/search/ingredient/{ingredient}/", response_model=list[RecipeSchema])
async def search_recipes_by_ingredient(ingredient: str):
    recipes = Recipe.objects.filter(ingredients__name__icontains=ingredient).distinct()
    return list(recipes)

@router.get("/recipes/category/{category_id}/", response_model=list[RecipeSchema])
async def get_recipes_by_category(category_id: int):
    try:
        category = Category.objects.get(pk=category_id)
        recipes = Recipe.objects.filter(categories=category)
        return list(recipes)
    except ObjectDoesNotExist:
        raise HTTPException(status_code=404, detail="Category not found")

@router.post("/recipes/", response_model=RecipeSchema)
async def create_recipe(recipe_data: RecipeSchema):
    # In a real implementation, you would need to handle author and relationships
    recipe = Recipe.objects.create(
        title=recipe_data.title,
        description=recipe_data.description,
        cooking_steps=recipe_data.cooking_steps,
        cooking_time=recipe_data.cooking_time,
        # author would need to be set based on authentication
    )
    return recipe

@router.put("/recipes/{recipe_id}/", response_model=RecipeSchema)
async def update_recipe(recipe_id: int, recipe_data: RecipeSchema):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
        for field, value in recipe_data.dict().items():
            setattr(recipe, field, value)
        recipe.save()
        return recipe
    except ObjectDoesNotExist:
        raise HTTPException(status_code=404, detail="Recipe not found")