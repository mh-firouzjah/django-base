from django.contrib import admin
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _


def perm_str(self) -> str:
    '''replace translate-marked strings'''
    if "add_" in self.codename:
        return _("Can add | {content_type}").format(
            content_type=self.content_type)
    elif "change_" in self.codename:
        return _("Can change | {content_type}").format(
            content_type=self.content_type)
    elif "delete_" in self.codename:
        return _("Can delete | {content_type}").format(
            content_type=self.content_type)
    # elif "view_" in self.codename:
    return _("Can view | {content_type}").format(
        content_type=self.content_type)


Permission.__str__ = perm_str


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser  # False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser
