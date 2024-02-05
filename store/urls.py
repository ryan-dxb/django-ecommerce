from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="store"),
    path("search/", views.search, name="search"),
    path("<slug:category_slug>/", views.index, name="store_by_category"),
    path(
        "<slug:category_slug>/<slug:product_slug>",
        views.product_detail,
        name="product_detail",
    ),
]
