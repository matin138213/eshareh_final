from django.contrib import admin

from word import models


# Register your models here.
class WordyAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category']


admin.site.register(models.Word)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'parent']


admin.site.register(models.Category)
