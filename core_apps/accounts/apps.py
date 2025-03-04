from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.accounts'
    def ready(self):
        import core_apps.accounts.signals
