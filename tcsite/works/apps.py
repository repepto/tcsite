from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'works'

    def ready(self):
        import works.signals
