from django.shortcuts import render, get_object_or_404,redirect
from django.template.response import TemplateResponse
from django.http import HttpResponse
#######3
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User, Tour, Comment
def index(request):
    return render(request, 'index.html')
# def user_detail(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     return render(request, 'users/detail.html', {'user': user})

# def tour_detail(request, tour_id):
#     tour = get_object_or_404(Tour, pk=tour_id)
#     comments = Comment.objects.filter(tour=tour)
#     return render(request, 'tours/detail.html', {'tour': tour, 'comments': comments})


# def add_comment(request, tour_id):
#     tour = get_object_or_404(Tour, pk=tour_id)
#     if request.method == 'POST':
#         author = request.POST.get('author')
#         text = request.POST.get('text')
#         comment = Comment(tour=tour, author=author, text=text)
#         comment.save()
#     return render(request, 'tours/detail.html', {'tour': tour})


# ########################################################
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

# @login_required(login_url='login')

# def user_logout(request):
#     logout(request)
#     return redirect('home')
# def user_register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # log the user in after registration
#             login(request, user)
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home') # replace 'home' with the name of your homepage view
#         else:
#             # handle invalid login credentials
#             pass
#     else:
#         # display the login form
#         return render(request, 'login.html')