# Para importar el sistema de formularios de django:
from django import forms 

#Django tiene incorporado un formulario diseñado especialmente para crear usuarios
from django.contrib.auth.forms import UserCreationForm

#Importar el modelo de usuario incorporado por django
from django.contrib.auth.models import User 

#Crear formulario de registro
class RegistroUsuarioForm(UserCreationForm):
    # Agregamos los campos explícitos para definir sus etiquetas 
    first_name = forms.CharField(
        label='Nombre',
        max_length=30,
        required=True
    )
    last_name = forms.CharField(
        label='Apellido',
        max_length=30,
        required=True
    )
    email = forms.EmailField(
        required=True,
        label='Correo electrónico'
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
        }
        help_texts = {
            'username': 'Requerido. 150 caracteres o menos. Letras, números y @/./+/-/_ solamente.',
        }