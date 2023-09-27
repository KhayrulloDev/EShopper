# from django.urls import path
#
# from .views import HomeView, ShopView, detail, contact, checkout, ShoppingCartView
#
# urlpatterns = [
#     path('', HomeView.as_view()),
#     path('shop', ShopView.as_view()),
#     path('detail', detail),
#     path('contact', contact),
#     path('checkout', checkout),
#     path('cart/', ShoppingCartView.as_view(), name='cart'),
# ]

# from django.urls import path
# from .views import HomeView, ShopView, detail, contact, checkout, ShoppingCartView
#
# urlpatterns = [
#     path('', HomeView.as_view(), name='home'),
#     path('shop/', ShopView.as_view(), name='shop'),
#     path('detail', detail, name='detail'),
#     path('contact', contact, name='contact'),
#     path('checkout', checkout, name='checkout'),
#     path('cart/', ShoppingCartView.as_view(), name='cart'),
# ]

from django.urls import path
from .views import HomeView, ShopView, detail, contact, checkout, ShoppingCartView, IncrementCountView, \
    DecrementCountView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop', ShopView.as_view(), name='shop'),
    path('detail', detail, name='detail'),
    path('contact', contact, name='contact'),
    path('checkout', checkout, name='checkout'),
    path('cart', ShoppingCartView.as_view(), name='cart'),
    path('increment-count', csrf_exempt(IncrementCountView.as_view()), name='increment'),
    path('decrement-count', csrf_exempt(DecrementCountView.as_view()), name='decrement'),
]
