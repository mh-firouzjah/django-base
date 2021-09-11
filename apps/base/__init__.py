from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.base'
    verbose_name = _("Base")

    def ready(self):
        import apps.base.utils.contenttype_translation_fix
