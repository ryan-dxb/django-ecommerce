from django.contrib import admin

from store.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "price",
        "stock",
        "created_at",
        "modified_at",
        "is_available",
    )
    prepopulated_fields = {"slug": ("product_name",)}


admin.site.register(Product, ProductAdmin)
