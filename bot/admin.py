from django.contrib import admin
from .models import Text, User

admin.site.register(Text)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_interaction')
    search_fields = ('user_id',)
    list_filter = ('first_interaction',)
    def has_add_permission(self, request):
        return False
