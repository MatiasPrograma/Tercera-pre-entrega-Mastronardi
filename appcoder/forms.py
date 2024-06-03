from django import forms

class clientes(forms.Form):
    
    nombre = forms.CharField( max_length=100)
    apellido = forms.CharField(max_length=20)
    
class ropa(forms.Form):
    Marca = forms.CharField(max_length=20)
    stock = forms.IntegerField()
    
class vendedor(forms.Form):
    
    Nombre = forms.CharField(max_length=20)
    idvendedor = forms.CharField(max_length=20)
    
class consultas(forms.Form):
    
    Problema = forms.CharField(max_length=40)
    idproblema = forms.IntegerField()

    
