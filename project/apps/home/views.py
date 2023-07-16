from django.shortcuts import render
from .forms import HomeForm
# Create your views here.

def index(request):
    return render(request, "cliente/index.html", {"saludo": "Holaaaa"})

def crear_cliente(request: HttpRequest):
    
    if request.method  == "POST":
        ...
    else:
        form = HomeForm()
    
    return render(request, "cliente/crear.html", {"form": form})
