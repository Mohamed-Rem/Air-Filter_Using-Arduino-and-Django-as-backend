from django.apps import AppConfig


class AppForTestingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_for_testing'
