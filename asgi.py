import os

from asgiref.typing import ASGIApplication
from django.core.asgi import get_asgi_application
from fastapi import FastAPI

# Установите настройки Django ДО импорта моделей
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_Recipe_Website.settings")
django_asgi_app = get_asgi_application()

# Импортируйте FastAPI компоненты ПОСЛЕ инициализации Django
from recipe_app.api.endpoints import router

app = FastAPI()
app.include_router(router)

# Комбинированное приложение (опционально)
combined_app = ASGIApplication(
    router={
        'http': app,
        'websocket': django_asgi_app,
    }
)