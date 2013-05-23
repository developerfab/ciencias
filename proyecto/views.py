# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

"""
Esta funcion se encarga de retornar la pagina principal del sitio
"""

def index(requests):
    print 'entra Index'
    dic={'bienvenido':'Transportes mi pais'}
    return render(requests,'proyecto/index.html',dic)

"""
Esta funcion retorna el sitio para registrar un nodo
"""
def registro(requests):
    
    dic={'bienvenido':'Transportes mi pais'}
    if requests.method == 'POST':
        print 'entra'
        nombre=requests.POST['nombre'] 
        x=int(requests.POST['cordX'])
        y=int(requests.POST['cordY'])
        print x
        print y 
        print nombre
    return render(requests,'proyecto/registro.html',dic)

    
    