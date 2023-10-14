from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Region

admin.site.register(Region)

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'password', 'email', 'region')  # Определите поля, которые должны отображаться в списке
    list_filter = ('region',)  # Добавьте фильтр по полю "region"
    search_fields = ('username', 'email')  # Добавьте поле для поиска
