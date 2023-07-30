from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


@login_required
def make_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.user = request.user
            review.save()
            return redirect('reviews_show')
    else:
        form = ReviewForm()
    reviews = Review.objects.order_by('-created_at')
    return render(request, 'write_review.html', {'form': form, 'reviews': reviews})


def review_show(request):
    reviews = Review.objects.order_by('-created_at')
    return render(request, 'review_show.html', {'reviews': reviews})
