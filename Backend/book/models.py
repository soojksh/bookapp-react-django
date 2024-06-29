from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.name



