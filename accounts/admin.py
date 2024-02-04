from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "date_joined",
        "last_login",
    )
    readonly_fields = ("date_joined", "last_login")
    list_display_links = ("email", "username")
    search_fields = ("email", "username")
    list_filter = ()
    filter_horizontal = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
