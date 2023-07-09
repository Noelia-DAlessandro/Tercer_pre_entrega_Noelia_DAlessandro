from django.http import HttpResponse

def saludo(request):

	return HttpResponse("Hola Django - Coder")

def saludo_vista(resquest):
    return HttpResponse("<h1>Segunda vista")

def nombre(resquest, nombre:str , apellido:str):
    nombre = nombre.capitalize ()
    apellido= apellido.capitalize ()
    return HttpResponse(f"{apellido}, {nombre}")
