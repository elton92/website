from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nome_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nome_usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect("home")
        else:
            messages.error(request, "Dados incorrectos...")

    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})

class VistaRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro.html", {"form":form})
    def postes(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nome_usuario = form.cleaned_data("username")
            messages.success(request, F"Benvido a plantaforma {nome_usuario}")
            login(request, usuario)
            return redirect("home")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro.html", {"form":form})
def sair(reques):
    logout(reques)
    return redirect("home")
