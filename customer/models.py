from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Customer(models.Model):
    username = models.OneToOneField(User, related_name="user_profile", verbose_name="Логин", unique=True, blank=True,
                                    null=True, default=None, on_delete=models.CASCADE)
    surname = models.CharField(verbose_name="Фамилия", max_length=255, blank=True, null=True, default=None)
    first_name = models.CharField(verbose_name="Имя", max_length=255, blank=True, null=True, default=None)
    last_name = models.CharField(verbose_name="Отчество", max_length=255, blank=True, null=True, default=None)
    email = models.EmailField(verbose_name="Электронная почта", blank=True, null=True, default=None)
    address = models.CharField(verbose_name="Адрес", max_length=255, blank=True, null=True, default=None)
    is_admin = models.BooleanField(verbose_name="Админ", default=False)
    phone_number = PhoneNumberField(null=True, default='+1234567890')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return f"{self.username}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(username=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()
