from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.ImageField(upload_to='pics')
    description = models.TextField()


class ShoppingCard(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    uploaded = models.DateTimeField(auto_now_add=True)