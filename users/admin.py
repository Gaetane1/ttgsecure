from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'statut', 'is_staff', 'is_active']
    list_filter = ['statut', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('statut', 'photo', 'adresse', 'telephone')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('statut', 'photo', 'adresse', 'telephone')}),
    )

admin.site.register(User, CustomUserAdmin)
