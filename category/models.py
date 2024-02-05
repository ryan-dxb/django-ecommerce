from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    category_image = models.ImageField(
        upload_to="photos/categories", blank=True, null=True
    )

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def get_url(self):
        return reverse("store_by_category", kwargs={"category_slug": self.slug})

    def __str__(self):
        return self.category_name
