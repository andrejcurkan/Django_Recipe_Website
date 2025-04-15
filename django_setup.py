import os
import django
from django.conf import settings

def setup_django():
    if not settings.configured:
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE",
            "Django_Recipe_Website.settings"  # Убедитесь, что это правильное имя!
        )
        django.setup()