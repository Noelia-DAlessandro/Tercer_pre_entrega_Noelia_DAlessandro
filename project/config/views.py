from django.http import HttpResponse
from django.shortcuts import render
#from django.template import Context, Template 

def saludo(request):

	return HttpResponse("Hola Django - Coder")

def saludo_vista(request):
    return HttpResponse("<h1>Segunda vista")

def nombre(request, nombre:str , apellido:str):
    nombre = nombre.capitalize ()
    apellido= apellido.capitalize ()
    return HttpResponse(f"{apellido}, {nombre}")

def probando_template(request):
	#mi_html = open("./templates/template1.html")
	#mi_template = Template(mi_html.read())
	#mi_html.close()
	nombre= "Louis"
	apellido= "Van Beethoven"
	datos={"nombre": nombre, "apellido": apellido}
	#mi_contexto = Context(datos)
	#mi_documento = mi_template.render(mi_contexto)
	#return HttpResponse(mi_documento)
	return render (request,"template1.html",datos)

def mis_notas(request):
    lista_de_notas = [2,6,8,9,7,6,9]
    contexto = {"notas": lista_de_notas}
    return render (request, "notas.html", contexto)
