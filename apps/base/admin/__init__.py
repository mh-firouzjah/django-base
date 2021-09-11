from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .permission import PermissionAdmin

admin.autodiscover()

admin.site.site_header = _('My Site Header')
admin.site.site_title = _('My Site Title')
admin.site.index_title = _('My Site Index Title')
