from django.contrib import admin
from other_info.models import UserInfo

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    pass
