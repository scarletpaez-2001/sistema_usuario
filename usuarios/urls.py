#Importar path:
from django.urls import path 

#Importar las vistas:
from . import views 

urlpatterns = [
    #Dirección- Registro
    path(
        'registro/',
        views.registro,
        name='registro'
    ),
]