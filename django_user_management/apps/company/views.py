from django.shortcuts import render, redirect
from apps.main.forms import LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password, group_name="CONTRACTOR")
        print(user)
        if user:
            login(request, user)
            # update_last_login(None, user)  # Disable updating last_login
            return redirect("/home")  # Redirect to the dashboard after login
        else:
            print("Invalid credentials")
    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {"form": form})