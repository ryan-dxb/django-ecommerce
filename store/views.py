from django.shortcuts import render, get_object_or_404, redirect

from cart.models import CartItem
from cart.views import _cart_id
from category.models import Category
from store.models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


def index(request, category_slug=None):
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
        product_count = products.count()

    else:
        products = Product.objects.all().filter(is_available=True).order_by("id")
        product_count = products.count()
        paginator = Paginator(products, 6)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)

    context = {"products": paged_products, "product_count": product_count}

    return render(request, "store/store.html", context)


def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request), product=product
        ).exists()

    except Exception as e:
        raise e

    context = {"product": product, "in_cart": in_cart}

    return render(request, "store/product_detail.html", context)


def search(request):
    products = Product.objects.all()
    product_count = products.count()
    context = {"products": products, "product_count": product_count}

    if "keyword" in request.GET:
        keyword = request.GET.get("keyword")

        if keyword is not None:
            products = products.filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
            )
            paginator = Paginator(products, 6)
            page = request.GET.get("page")
            paged_products = paginator.get_page(page)
            product_count = products.count()
            context["products"] = paged_products
            context["product_count"] = product_count
            context["keyword"] = keyword
        else:
            return render(request, "store/store.html", context)

    return render(request, "store/store.html", context)
