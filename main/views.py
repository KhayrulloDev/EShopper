import json

from django.shortcuts import render, redirect
from django.views import View
from .models import Product, ShoppingCard
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

from .utils import increment_count, decrement_count


class HomeView(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'index.html', {'products': products})

    def post(self, request):
        pass


class ShopView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'shop.html', {'products': products})

    def post(self, request):
        id = request.POST.get('id')
        user_id = request.user.id
        shopping_card = ShoppingCard.objects.create(
            product_id=id,
            user_id=user_id,
        )
        shopping_card.save()
        messages.info(request, 'Added successfully')
        return redirect('shop')


def detail(request):
    return render(request, 'detail.html')


def contact(request):
    return render(request, 'contact.html')


def checkout(request):
    return render(request, 'checkout.html')


class ShoppingCartView(View):
    template_name = 'cart.html'
    context = {}

    def get(self, request):
        shopping_card = ShoppingCard.objects.filter(user=request.user).values('product_id')
        products = Product.objects.filter(pk__in=shopping_card)
        data = []
        for product in products:
            shop = ShoppingCard.objects.get(Q(user=request.user) & Q(product=product))
            product.count = shop.count
            data.append(product)
        self.context.update({'products': data})
        return render(request, self.template_name, self.context)

    def post(self, request):
        id = request.POST.get('id')
        user = request.user
        shopping_card = ShoppingCard.objects.get(Q(product_id=id) & Q(user=user))
        shopping_card.delete()
        return redirect('cart')


class IncrementCountView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            id = json_data.get('id')
        except json.JSONDecodeError:
            id = None
        result = increment_count(id, request.user)
        return JsonResponse({'result': result})


class DecrementCountView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            id = json_data.get('id')
        except json.JSONDecodeError:
            id = None
        result = decrement_count(id, request.user)
        return JsonResponse({'result': result})
