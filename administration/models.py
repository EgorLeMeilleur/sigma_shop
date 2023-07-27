from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Administration(models.Model):
    username = models.OneToOneField(User, related_name="profile", verbose_name="Логин", unique=True, blank=True,
                                    null=True, default=None, on_delete=models.CASCADE)
    surname = models.CharField(verbose_name="Фамилия", max_length=255, blank=True, null=True, default=None)
    first_name = models.CharField(verbose_name="Имя", max_length=255, blank=True, null=True, default=None)
    last_name = models.CharField(verbose_name="Отчество", max_length=255, blank=True, null=True, default=None)
    email = models.EmailField(verbose_name="Электронная почта", blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f"{self.username}"

