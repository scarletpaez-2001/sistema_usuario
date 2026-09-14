#Render permite cargar un archivo HTML. Redirect permitge enviar al usuario hacia otra página.
from django.shortcuts import render, redirect 

#Importar nuestro primer formulario:
from .forms import RegistroUsuarioForm

#Vista responsable del registro:
def registro(request):

    #Comporbamos si el navegador está enviando información mediante POST.
    if request.method == 'POST':

        #Creamos un formulario utilizando la información recibida
        form = RegistroUsuarioForm(
            request.POST
        )

        #Verificamos que los datos sean válidos:
        if form.is_valid():

            #Guardamos el usuario, Django se encargará de almacenarlo en la base de datos:
            form.save()

            #Después del registro enviamos al usuario a la página del loggin:
            return redirect('login')

        else:

            #Si solamente estamos entrando a la página, creamos un formulario vacío:
            form = RegistroUsuarioForm()

        #Mostramos el archivo HTML:
        return render(
            request,
            'usuarios/registro.html',
            {
                'form' : form
            }
        )

        