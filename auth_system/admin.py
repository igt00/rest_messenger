from django.contrib import admin
from auth_system.models import User2


class User2Admin(admin.ModelAdmin):
    search_fields = ('first_name', 'second_name', 'surname')


admin.site.register(User2, User2Admin)
