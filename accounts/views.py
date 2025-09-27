from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render

from accounts.forms import LoginForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("core:home")
            else:
                form.add_error(None, "نام کاربری یا رمز عبور اشتباه است")
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def auth_logout(request):
    pass


def logout_view(request):
    auth_logout(request)
    return redirect('accounts:login')
