from django.db import models

# Create your models here.
from customer.models import Customer
from products.models import Product


class Purchase(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='purchases')
    benefit = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} bought {self.benefit.name} on {self.date}'

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
