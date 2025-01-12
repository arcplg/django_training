from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth.models import User, update_last_login
from core.auth_backends import AdminAuthBackend
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
@login_required(login_url="/login")
def home(request, *args, **kwargs):
    posts = Post.objects.all()
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        print(post_id)
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
    return render(request, 'main/home.html', {"posts": posts})

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {"form": form})

def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password, group_name="APG")
        print(user)
        if user:
            login(request, user)
            # update_last_login(None, user)  # Disable updating last_login
            return redirect("/home")  # Redirect to the dashboard after login
        else:
            print("Invalid credentials")
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {"form": form})

@login_required(login_url="/login")
def create_post(request, *args, **kwargs):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm
    return render(request, "main/create_post.html", {"form": form})

def log_out(request):
    logout(request)
    return redirect('/home')
