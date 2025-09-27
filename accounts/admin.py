from django.contrib import admin
from accounts.models import User

@admin.register(User)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')