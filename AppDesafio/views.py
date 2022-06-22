from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Prueba

# Create your views here.

def una_vista(request):
    return HttpResponse('<h1>Hola Mundo</h1>')

def un_template(request):
    
    #template = loader.get_template('index.html')
    
    prueba1=Prueba(nombre='Pepito')
    prueba2=Prueba(nombre='Pepito2')
    prueba3=Prueba(nombre='Pepito3')
    
    #render = template.render({'lista_objeto': [prueba1,prueba2,prueba3]})
    
    return render(request, 'index.html', {'lista_objeto': [prueba1,prueba2,prueba3]})