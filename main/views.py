from django.shortcuts import render
from django.views import View
from .models import Product


class HomeView(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'index.html', {'products': products})

    def post(self, request):
        pass


def shop(request):
    return render(request, 'shop.html')


def detail(request):
    return render(request, 'detail.html')


def contact(request):
    return render(request, 'contact.html')


def checkout(request):
    return render(request, 'checkout.html')


def cart(request):
    return render(request, 'cart.html')


