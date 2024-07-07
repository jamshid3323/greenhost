from django.apps import AppConfig


class HostingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hostings'

    def ready(self):
        from . import signals
