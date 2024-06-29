from django.contrib import admin
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_editable = ['price']

class CategoryAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ('name',)

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
