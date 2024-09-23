from django.contrib import admin
from other_info.models import UserInfo, News, NewData

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(NewData)
class NewDataAdmin(admin.ModelAdmin):
    pass