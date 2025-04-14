from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Recipe, Category, Ingredient, RecipeIngredient
from django.forms import inlineformset_factory
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    pass


class RecipeForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cooking_steps', 'cooking_time', 'image', 'categories']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'cooking_steps': forms.Textarea(attrs={'rows': 5}),
        }


class IngredientForm(forms.Form):
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all())
    quantity = forms.CharField(max_length=50, required=False)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']