from django.contrib import admin
from .models import UserProfile


def make_Manager(modeladmin, request, queryset):
    queryset.update(is_manager=True)
make_Manager.short_description = "Mark selected User as Manager"

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username','email','full_name','is_active','is_manager')
    exclude = (
        'password','groups',
        'user_permissions','last_login',
        'date_joined','is_superuser',
        'is_staff',
        )
    actions = [make_Manager]

    def full_name(self,obj):
        return "%s %s" % (obj.first_name, obj.last_name)

admin.site.register(UserProfile, UserProfileAdmin)

