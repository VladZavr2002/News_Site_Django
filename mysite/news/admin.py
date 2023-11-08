from django.contrib import admin
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):  #Налаштування моделі в admin для додавання більшої інформації
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)#Поставити кому, так як це кортеж, а не рядок


admin.site.register(News, NewsAdmin)# Спочатку треба оголосити модель News, а вже потім клас де модель налаштовується
admin.site.register(Category, CategoryAdmin)
