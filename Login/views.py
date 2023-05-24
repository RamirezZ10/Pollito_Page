from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import glob, os

# Create your views here.

def Login(request):
    if request.method == "POST":
        user = request.POST["user"]
        password = request.POST["password"]

        if user == "Pollito" and password == "06-03":
            request.session["user"] = user
            return redirect("Fotitos")

    if request.method == "GET":
        try:
            del request.session["user"]
        except Exception as e:
            pass

    return render(request, "Login.html", {
                      "Title":"Login"
                  })

def Fotitos(request):
    user = request.session.get("user")
    if user is not None:
        numbers = range(0, 32)
        return render(request, "Fotitos.html", 
                      {
                          "Title": "Nuestras Fotitos",
                          "numbers": numbers
                      })
    else:
        return redirect("Login")

def Dibujos(request):
    user = request.session.get("user")
    if user is not None:
        numbers = range(0, 110)

        return render(request, "Dibujos.html", 
                      {
                          "Title": "Nuestros Dibujos",
                          "numbers": numbers
                      })
    else:
        return redirect("Login")
