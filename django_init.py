import os
import django
from django.conf import settings

def init_django():
    if not settings.configured:
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE",
            "Django_Recipe_Website.settings"  # Убедитесь, что имя проекта правильное!
        )
        django.setup()