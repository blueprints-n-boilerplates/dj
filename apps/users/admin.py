from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Address, AccountSettings


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('User Details', {
            'fields': (
                'email',
                'password',
                'first_name',
                'middle_name',
                'last_name',
                'birth_date',
                'is_verified',
                'is_staff',
                'is_superuser',
                'is_active',
                'last_login',
                'gender',
            )
        }),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )
    list_display = (
        'id',
        'email',
        'first_name',
        'middle_name',
        'last_name',
        'gender',
    )
    list_filter = (
        'is_staff',
        'is_superuser',
        'is_active',
        'is_verified',
        'groups',
    )
    search_fields = ('id', 'email')
    ordering = ('id', 'email',)
    filter_horizontal = ('groups', 'user_permissions')
    readonly_fields = (
        'last_login',
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Address)
admin.site.register(AccountSettings)
