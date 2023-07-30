from django.urls import path
from reviews import views

urlpatterns = [
    path('make_review/', views.make_review, name='make_review'),
    path('review/', views.review_show, name='review_show'),
]
