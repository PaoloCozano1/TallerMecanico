
from django.shortcuts import render, redirect
from matplotlib import image
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required,permission_required
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"app/index.html")

def galeria(request):
    return render(request,"app/galeria.htm")

def autos_cristian(request):
    return render(request,"app/autos_cristian.htm")

def autos_sebastian(request):
    return render(request,"app/autos_sebastian.htm")

def contacto(request):
    data ={
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"]
    return render(request,"app/contacto.htm", data)

def cristian(request):
    return render(request,"app/cristian.htm")

def login(request):
    return render(request,"registration/login.htm")

def registro(request):
    datos ={
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        datos["form"] = formulario
    return render(request,"registration/registro.htm",datos)

def sebastian(request):
    return render(request,"app/sebastian.htm")

def newatencion(request):
    data = {
        'form': AtencionForm()
    }
    if request.method=='POST':
        formulario = AtencionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'app/newatencion.html',data)

def atencion(request):
    atenciones = Atencion.objects.all()
    data = {
        'atenciones': atenciones
    }
    return render(request, 'app/atencion.html',data)