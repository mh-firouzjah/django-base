'''
this module fixes translation issues of django's default `Permission` class
'''
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _


def perm_str(self) -> str:
    '''fixes translation issues by inserting translation-marked strings'''
    if "add_" in self.codename:
        return _("Can add | %s") % self.content_type
    if "change_" in self.codename:
        return _("Can change | %s") % self.content_type
    if "delete_" in self.codename:
        return _("Can delete | %s") % self.content_type
    # elif "view_" in self.codename:
    return _("Can view | %s") % self.content_type

# monkey patche for `Permission` class `__str__` method
Permission.__str__ = perm_str


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    '''register `Permission` to admin panel
        *this part could be ignored.
    '''
    def has_add_permission(self, request):
        return request.user.is_superuser  # False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser
