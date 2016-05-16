from django.apps import AppConfig


class AboutConfig(AppConfig):
    name = 'about'

    def ready(self):
        import about.signals
