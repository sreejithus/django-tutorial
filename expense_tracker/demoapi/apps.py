from django.apps import AppConfig


class DemoapiConfig(AppConfig):
    name = 'demoapi'
    def ready(self):
           from . import signals

           
