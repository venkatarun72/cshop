from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=50, blank=True, null=True, default='')
    image = models.ImageField(upload_to='Product')


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryID(category_id):
        return Product.objects.filter(category=category_id)
