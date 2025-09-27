from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return HttpResponse("Hello, world. You're at the login page.")


def logout(request):
    return HttpResponse("Logged out.")
