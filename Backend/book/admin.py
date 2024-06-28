from django.contrib import admin
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_editable = ['price']