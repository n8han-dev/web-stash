# starter_page/admin.py
from django.contrib import admin
from .models import Article, PageSection

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "published")
    prepopulated_fields = {"slug": ("title",)}  # auto-generate slug from title

@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ("name",)