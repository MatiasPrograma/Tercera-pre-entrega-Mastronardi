from django.shortcuts import render
from .forms import *
from .models import *


def inicio(req):
    
    return render(req, 'inicio.html',{})

def ropavista(req):
    if req.method == 'POST':
        miFormulario = ropa(req.POST)
        if miFormulario.is_valid():
            Marca = miFormulario.cleaned_data['Marca']
            stock = miFormulario.cleaned_data['stock']
            
            nueva_ropa = Ropa(Marca=Marca, stock=stock)
            nueva_ropa.save()
            
            return render(req, 'inicio.html', {'miFormulario': miFormulario})
    else:
        miFormulario = ropa()
        return render(req, 'ropa.html',{'miFormulario': miFormulario})

def vendedorvista(req):
    if req.method == 'POST':
        miFormulario = vendedor(req.POST)
        if miFormulario.is_valid():
            Nombre = miFormulario.cleaned_data['Nombre']
            idvendedor = miFormulario.cleaned_data['idvendedor']
            
            nuevo_vendedor = Vendedor(nombre=Nombre, idvendedor=idvendedor)
            nuevo_vendedor.save()
            
            return render(req, 'inicio.html', {'miFormulario': miFormulario})
    else:
        miFormulario = vendedor()
        return render(req, 'vendedor.html',{'miFormulario': miFormulario})

def consultasvista(req):
    if req.method == 'POST':
        miFormulario = consultas(req.POST)
        if miFormulario.is_valid():
            problema = miFormulario.cleaned_data['problema']
            idproblema = miFormulario.cleaned_data['idproblema']
            
            nueva_consulta = Consultas(Problema=problema, idproblema=idproblema)
            nueva_consulta.save()
            
            return render(req, 'inicio.html', {'miFormulario': miFormulario})
    else:
        miFormulario = consultas()
        return render(req, 'consultas.html',{'miFormulario': miFormulario})

def clientesvista(req):
    if req.method == 'POST':
        miFormulario = clientes(req.POST)
        if miFormulario.is_valid():
            nombre = miFormulario.cleaned_data['nombre']
            apellido = miFormulario.cleaned_data['apellido']
            
            nuevo_cliente = Clientes(nombre=nombre, apellido=apellido)
            nuevo_cliente.save()
                        
            return render(req, 'inicio.html', {'miFormulario': miFormulario})
    else:
        miFormulario = clientes()
    return render(req, 'clientes.html', {'miFormulario': miFormulario})

def busquedacliente(req):
    
    return render(req,'busqueda.html')

def buscar(req):
    
    if req.GET["nombre"]:
        
        nombre = req.GET["nombre"]
        
        apellido = Clientes.objects.filter(nombre=nombre)
        
        return render(req, 'resultadobusqeda.html', {"nombre": nombre, "apellido": apellido})

    else:
        return render(req, "inicio.html")
