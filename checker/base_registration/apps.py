from django.apps import AppConfig


class BaseRegistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_registration'
