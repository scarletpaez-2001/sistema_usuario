# Para importar el sistema de formularios de django:
from django import forms 

#Django tiene incorporado un formulario diseñado especialmente para crear usuarios
from django.contrib.auth.forms import UserCreationForm

#Importar el modelo de usuario incorporado por django
from django.contrib.auth.models import User 

#Crear formulario de registro
#Heredamos de UserCreationForm para aprovevhar las validaciones de usuarios y contraseñas que django trae incorporada.
class RegistroUsuarioForm(UserCreationForm):


# Agregamos el correo electrónico porque queremos solicitarlo obligatoriamente. #
    email = forms.EmailField(
        required=True,
        label='Correo electrónico'
    )

    class Meta:

    #Indicamos que este formulario trabaja con el modelo user.
        model = User

    #Definimos los campos que aparecerán en nuestro formulario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
    ]
    