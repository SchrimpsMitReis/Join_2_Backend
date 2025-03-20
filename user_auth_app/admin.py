from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ("email", "name", "tel", "is_staff", "is_superuser")  # Zeigt Contact-Felder an
    search_fields = ("email", "name", "tel")  # Ermöglicht die Suche nach diesen Feldern
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),  # Login-Felder
        ("Personal Info", {"fields": ("name", "tel")}),  # Felder aus Contact
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "name", "tel", "is_staff", "is_superuser"),
        }),
    )

admin.site.register(Account, AccountAdmin)