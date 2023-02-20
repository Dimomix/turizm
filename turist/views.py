from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User, Tour, Comment
def index(request):
    return render(request, "templates/index.html")
def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/detail.html', {'user': user})

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    comments = Comment.objects.filter(tour=tour)
    return render(request, 'tours/detail.html', {'tour': tour, 'comments': comments})


def add_comment(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        comment = Comment(tour=tour, author=author, text=text)
        comment.save()
    return render(request, 'tours/detail.html', {'tour': tour})
