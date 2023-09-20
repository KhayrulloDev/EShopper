from django.urls import path

from .views import HomeView, shop, detail, contact, checkout, cart

urlpatterns = [
    path('', HomeView.as_view()),
    path('shop', shop),
    path('detail', detail),
    path('contact', contact),
    path('checkout', checkout),
    path('cart', cart),
]