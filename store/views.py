from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import category

# Create your views here.


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(category, slug=category_slug)
        Products = Product.objects.filter(category=categories, is_avalible=True)
        product_count = Products.count()
    else:
        products = Product.objects.all().filter(is_avalible=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    return render(request, 'store/product_detail.html')