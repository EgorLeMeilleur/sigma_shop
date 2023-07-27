from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from products.models import Product


class Wishes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_wish')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_wish')

    def __str__(self):
        return f'{self.user.username} wishes {self.product.name}'

    class Meta:
        verbose_name = 'Желание'
        verbose_name_plural = 'Желания'