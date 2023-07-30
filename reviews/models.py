from django.contrib.auth.models import User
from django.db import models


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_review')
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f'{self.user.username} reviewed on {self.text}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
