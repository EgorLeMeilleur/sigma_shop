from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255, unique=True, blank=True, null=True, default=None)
    price = models.DecimalField(verbose_name="Цена", max_digits=1000, decimal_places=2, blank=True, null=True,
                                default=None)
    description = models.CharField(verbose_name="Описание", max_length=255, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
