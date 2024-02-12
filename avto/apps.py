from django.apps import AppConfig


class AvtoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "avto"

    def ready(self):
        import avto.signals
