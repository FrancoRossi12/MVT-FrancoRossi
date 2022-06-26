from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Prueba

# Create your views here.

def una_vista(request):
    return render(request, 'index.html')

def un_template(request):
    
    #template = loader.get_template('index.html')
    
    prueba1=Prueba(nombre='Franco',edad='20',fecha_nacimiento='2001-11-19')
    prueba2=Prueba(nombre='Luca',edad='17',fecha_nacimiento='2005-7-19')
    prueba3=Prueba(nombre='Giuli',edad='14',fecha_nacimiento='2007-12-21')
    
    #render = template.render({'lista_objeto': [prueba1,prueba2,prueba3]})
    
    return render(request, 'mi_template.html', {'lista_objeto': [prueba1,prueba2,prueba3]})