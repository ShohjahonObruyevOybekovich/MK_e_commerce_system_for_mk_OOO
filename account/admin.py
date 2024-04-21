from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUser
from account.forms import CustomUserChangeForm, CustomUserCreationForm
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm,CustomUserCreationForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name", "phone", "photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups_joined")}),
        ("Important dates", {"fields": ("created_at", "updated_at")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups_joined", "name", "phone", "photo"
            )}
        ),
    )
    search_fields = ("email", "name", "phone")
    ordering = ("email",)

    change_form_template = 'admin/auth/user/user_change_form.html'

admin.site.register(CustomUser)