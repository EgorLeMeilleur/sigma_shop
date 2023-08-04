from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from products.models import Product


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases')
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    old = models.BooleanField(default=False, verbose_name="Выполненный заказ")

    def __str__(self):
        return f'{self.user.username} bought {self.product.name} on {self.date}'

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
