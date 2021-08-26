from apps.accounts.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': (
        'username', 'password1', 'password2', ), }), )

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_staff:
            if request.user.is_superuser:
                return ('last_login', 'date_joined')
            return ('is_staff', 'is_active', 'is_superuser', 'groups',
                    'user_permissions', 'last_login', 'date_joined')

    def has_add_permission(self, request):
        return request.user.is_superuser  # False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser
