from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
]