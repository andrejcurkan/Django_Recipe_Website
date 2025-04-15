from fastapi import APIRouter, HTTPException
from django.core.exceptions import ObjectDoesNotExist
from recipe_app.models import Recipe, Category, Ingredient
from .schemas import RecipeSchema, CategorySchema, IngredientSchema
from fastapi import APIRouter
from django_setup import setup_django  # Импортируем функцию настройки

# Инициализируем Django перед всеми импортами моделей
setup_django()

# Теперь безопасно импортируем модели
from recipe_app.models import Recipe, Category, Ingredient
from fastapi import APIRouter

# Не импортируйте модели здесь! Они будут импортированы после инициализации Django
router = APIRouter()

@router.get("/recipes")
async def get_recipes():
    from recipe_app.models import Recipe  # Ленивый импорт
    return {"recipes": list(Recipe.objects.all().values())}

@router.get("/recipes/{recipe_id}/", response_model=RecipeSchema)
async def get_recipe(recipe_id: int):from fastapi import APIRouter
from django_init import init_django  # Импортируем из текущей директории

# Инициализируем Django ПЕРЕД импортом моделей
init_django()

# Теперь безопасно импортируем модели
from recipe_app.models import Recipe, Category, Ingredient

router = APIRouter()

@router.get("/recipes")
async def get_recipes():
    return {"recipes": list(Recipe.objects.all().values())}
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