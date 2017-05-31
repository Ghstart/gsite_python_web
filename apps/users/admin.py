from django.contrib import admin

# Register your models here.
from .models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserInfo, UserInfoAdmin)