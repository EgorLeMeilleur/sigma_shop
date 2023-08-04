from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255, unique=True, blank=True, null=True, default=None)
    price = models.DecimalField(verbose_name="Цена", max_digits=8, decimal_places=2, blank=True, null=True,
                                default=None)
    description = models.TextField(verbose_name="Описание", max_length=255, blank=True, null=True, default=None)
    promotion = models.DecimalField(verbose_name="Акция", max_digits=5, decimal_places=2, blank=True, null=True, default=0)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_discounted_price(self):
        return self.price * (1 - self.promotion / 100)

    def get_purchase_count(self):
        return self.purchases.aggregate(total_quantity=models.Sum('quantity'))['total_quantity']


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Clothes(Product):
    size = models.CharField(max_length=10, null=True, default=None)
    color = models.CharField(max_length=20, null=True, default=None)
    material = models.CharField(max_length=20, null=True, default=None)
    product_ptr = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )

    class Meta:
        verbose_name = 'Одежда'


class TShirt(Clothes):
    clothes_ptr = models.OneToOneField(
        Clothes,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )

    class Meta:
        verbose_name = 'Футболка'
        verbose_name_plural = 'Футболки'


class Sweatshirt(Clothes):
    clothes_ptr = models.OneToOneField(
        Clothes,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )

    class Meta:
        verbose_name = 'Свитшот'
        verbose_name_plural = 'Свитшоты'


class Hoody(Clothes):
    clothes_ptr = models.OneToOneField(
        Clothes,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )

    class Meta:
        verbose_name = 'Худи'
        verbose_name_plural = 'Худи'
