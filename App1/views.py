from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Client, Order, Product
from django.db.models import Q
from django.http import HttpResponse

def home(request):
    return HttpResponse("Добро пожаловать на главную страницу!")

def client_orders(request, client_id):
    orders = Order.objects.filter(client_id=client_id).prefetch_related('products')
    return render(request, 'client_orders.html', {'orders': orders})


def client_products(request, client_id, period_days):
    period = timezone.now() - timedelta(days=period_days)
    orders = Order.objects.filter(client_id=client_id, order_date__gte=period)
    products_ids = orders.values_list('products', flat=True).distinct()
    products = Product.objects.filter(id__in=products_ids)
    return render(request, 'client_products.html', {'products': products, 'period_days': period_days})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})


def client_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'client_detail.html', {'client': client})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_detail.html', {'order': order})