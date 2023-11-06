from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("consultas/", views.consultas, name="consultas"),
    path("lista-general/", views.lista_general, name="lista_general"),
    path("administrador/", views.loginhtml, name="login"),
    path("administrador/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "agregar-clientes/",
        views.agregar_clientes,
        name="agregar_clientes",
    ),
    path(
        "editar-clientes/<int:id_cliente>",
        views.editar_clientes,
        name="editar_clientes",
    ),
    path(
        "actualizar-cliente/<int:id_cliente>",
        views.actualizar_cliente,
        name="actualizar_cliente",
    ),
    path(
        "eliminar-cliente/<int:id_cliente>",
        views.eliminar_clientes,
        name="eliminar_clientes",
    ),
    path(
        "agregar-medicos/",
        views.agregar_medicos,
        name="agregar_medicos",
    ),
    path(
        "editar-medico/<int:id_medico>",
        views.editar_medicos,
        name="editar_medicos",
    ),
    path(
        "actualizar-medico/<int:id_medico>",
        views.actualizar_medico,
        name="actualizar_medico",
    ),
    path(
        "eliminar-medico/<int:id_medico>",
        views.eliminar_medicos,
        name="eliminar_medicos",
    ),
    path(
        "superuser-login/", views.SuperuserLoginView.as_view(), name="superuser-login"
    ),
    path(
        "consultas/person_create/",
        views.ClienteCreateView.as_view(),
        name="person_create",
    ),
    path(
        "consultas/doctor_create/",
        views.MedicoCreateView.as_view(),
        name="doctor_create",
    ),
    # Nueva ruta para la vista combinada
    path(
        "consultas/cliente_medico_create/",
        views.ClienteMedicoCreateView.as_view(),
        name="cliente_medico_create",
    ),
]
