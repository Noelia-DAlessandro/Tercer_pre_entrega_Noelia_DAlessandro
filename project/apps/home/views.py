from django.shortcuts import render
from .forms import HomeForm
# Create your views here.

def index(request):
    return render(request, "cliente/index.html", {"saludo": "Holaaaa"})

def crear_cliente(request: HttpRequest) -> HttpResponse:
    
    if request.method  == "POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(cliente:home)
            
    else:
        form = HomeForm()
    
    return render(request, "cliente/crear.html", {"form": form})
