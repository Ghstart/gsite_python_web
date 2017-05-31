from django.contrib import admin

# Register your models here.
from .models import News

class NewsAdmin(admin.ModelAdmin):
    pass

admin.site.register(News, NewsAdmin)
