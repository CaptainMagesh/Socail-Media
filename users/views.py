from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import SignupForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redirect to home after signup
    else:
        form = UserCreationForm()

    return render(request, "users/signup.html", {"form": form})
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect to home after login
    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})
@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            new_password=form.cleaned_data["new_password1"]
            if new_password in request.user.past_passwords:
                form.add_error("new_password1","You cannot use the previous password")
            else:
                user=form.save
                user.save_password(new_password)
                update_session_auth_hash(request,user)
                return redirect("home")
    else:
        form=PasswordChangeForm(request.user)
    return render (request,"change_password.html",{"form":form})


def home(request):
    return render(request, "home.html")
