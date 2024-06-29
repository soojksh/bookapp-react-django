from django.shortcuts import render
from . models import Book, Category
from . serializers import BookSerializer, CategorySerializer
from rest_framework import viewsets


class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

