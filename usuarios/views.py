# Render permite cargar un archivo HTML. Redirect permite enviar al usuario a otra URL.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Importar nuestro primer formulario
from .forms import RegistroUsuarioForm

# Vista responsable del registro 
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
        
    return render(
        request,
        'usuarios/registro.html',
        {
            'form': form
        }
    )

# NUEVA VISTA: Pagina a la que llega el usuario al iniciar sesión
@login_required
def bienvenida(request):
    return render(request, 'usuarios/bienvenida.html')

# Importamos el modelo de usuarios de Django
from django.contrib.auth.models import User

# VISTA PARA LISTAR USUARIOS Y ROLES
@login_required
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

# VISTA PARA EDITAR PERFIL
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()
        return redirect('bienvenida')
        
    return render(request, 'usuarios/editar_perfil.html')