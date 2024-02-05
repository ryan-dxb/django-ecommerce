from django.db import models
from category.models import Category
from django.shortcuts import reverse


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to="photos/products", blank=True, null=True)
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse(
            "product_detail",
            kwargs={"category_slug": self.category.slug, "product_slug": self.slug},
        )
