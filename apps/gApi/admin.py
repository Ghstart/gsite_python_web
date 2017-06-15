from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import News, jobbole_date, jobbole_detail_data, jobbole_image_data

class NewsAdmin(admin.ModelAdmin):
    pass

class jobbole_dateAdmin(admin.ModelAdmin):
    list_display = ('custom_description', 'show_detail_info_url', 'publish_time', 'location', 'fav_num')

    def show_detail_info_url(self, obj):
        return format_html("<a href='{url}' target='_blank'>{url}</a>", url=obj.detail_info_url)
    show_detail_info_url.short_description = "详情链接"

class jobbole_detail_dataAdmin(admin.ModelAdmin):
    list_display = ('show_detail_description_content',)

    def show_detail_description_content(self, obj):
        return format_html("<pre>{url}</pre>", url=obj.detail_description_content)
    show_detail_description_content.short_description = "自我介绍"


class jobbole_image_dataAdmin(admin.ModelAdmin):
    list_display = ('show_image_url',)

    def show_image_url(self, obj):
        return format_html("<a href='{url}' target='_blank'>{url}</a>", url=obj.image_url)
    show_image_url.short_description = "自拍链接"

admin.site.register(News, NewsAdmin)
admin.site.register(jobbole_date, jobbole_dateAdmin)
admin.site.register(jobbole_detail_data, jobbole_detail_dataAdmin)
admin.site.register(jobbole_image_data, jobbole_image_dataAdmin)
