from django.urls import path
from appcoder.views import *

urlpatterns = [
    path('', inicio , name='inicio'),
    path('ropa/', ropavista , name='ropa'),
    path('clientes/', clientesvista , name='clientes'),
    path('consultas/', consultasvista , name='consultas'),
    path('vendedor/', vendedorvista , name='vendedor'),
    path('busquedacliente/', busquedacliente , name= 'busquedacliente'),
    path('resultadobusqueda/', buscar , name= 'buscar')
    
]
