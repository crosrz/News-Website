from django.contrib import admin
from .models import Category, News, Comment


class CategoryDisplay(admin.ModelAdmin):
    list_display = ("category_order", "category_title")


admin.site.register(Category, CategoryDisplay)


class AdminNews(admin.ModelAdmin):
    list_display = ("news_title", "category", "news_author", "news_time")


admin.site.register(News, AdminNews)


class AdminComment(admin.ModelAdmin):
    list_display = ("news", "email", "comment", "status")


admin.site.register(Comment, AdminComment)
