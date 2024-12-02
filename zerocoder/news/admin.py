from django.contrib import admin
from .models import News_post

class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'pub_date', 'author')

admin.site.register(News_post, NewsPostAdmin)