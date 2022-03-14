from django.apps import AppConfig


class SemanticConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'semantic'

    def ready(self) -> None:
        import semantic.signals
        return super().ready()

