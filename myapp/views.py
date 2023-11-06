from django.views.generic.edit import CreateView
from django.views import View
from django.db import transaction
from django.shortcuts import render, redirect
from .models import Clientes, Medicos
from .forms import ClienteForm, MedicoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView


def index(request):
    return render(request, "index.html")


def consultas(request):
    return render(request, "consultas.html")


def loginhtml(request):
    return render(request, "login.html")


def lista_general(request):
    clientes = Clientes.objects.all()
    medicos = Medicos.objects.all()
    return render(
        request,
        "templates_admin/listasGenerales.html",
        {"clientes": clientes, "medicos": medicos},
    )


# funciones para listar, editar y eliminar Clientes
def editar_clientes(request, id_cliente):
    cliente = Clientes.objects.filter(id=id_cliente).first()
    form = ClienteForm(instance=cliente)
    return render(
        request,
        "templates_admin/editarClientes.html",
        {"form": form, "cliente": cliente},
    )


def actualizar_cliente(request, id_cliente):
    cliente = Clientes.objects.get(pk=id_cliente)
    form = ClienteForm(request.POST, instance=cliente)
    if form.is_valid():
        form.save()
    clientes = Clientes.objects.all()
    medicos = Medicos.objects.all()
    return render(
        request,
        "templates_admin/listasGenerales.html",
        {"clientes": clientes, "medicos": medicos},
    )


def eliminar_clientes(request, id_cliente):
    cliente = Clientes.objects.get(pk=id_cliente)
    cliente.delete()
    clientes = Clientes.objects.all()
    medicos = Medicos.objects.all()
    return render(
        request,
        "templates_admin/listasGenerales.html",
        {"clientes": clientes, "medicos": medicos, "mensaje": "OK"},
    )


# funciones para listar, agregar, editar y eliminar Medicos
def agregar_medicos(request):
    if request.method == "POST":
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MedicoForm()
    return render(request, "templates_admin/agregarMedicos.html", {"form": form})


def editar_medicos(request, id_medico):
    medico = Medicos.objects.filter(id=id_medico).first()
    form = MedicoForm(instance=medico)
    return render(
        request,
        "templates_admin/editarMedicos.html",
        {"form": form, "medico": medico},
    )


def actualizar_medico(request, id_medico):
    medico = Medicos.objects.get(pk=id_medico)
    form = MedicoForm(request.POST, instance=medico)
    if form.is_valid():
        form.save()
    clientes = Clientes.objects.all()
    medicos = Medicos.objects.all()
    return render(
        request,
        "templates_admin/listasGenerales.html",
        {"medicos": medicos, "clientes": clientes},
    )


def eliminar_medicos(request, id_medico):
    medico = Medicos.objects.get(pk=id_medico)
    medico.delete()
    medicos = Medicos.objects.all()
    clientes = Clientes.objects.all()
    return render(
        request,
        "templates_admin/listasGenerales.html",
        {"medicos": medicos, "clientes": clientes, "mensaje_m": "OK"},
    )


class SuperuserLoginView(LoginView):
    template_name = "login.html"

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(self.request, user)
            return redirect("lista_general")
        return super().form_valid(form)


class ClienteCreateView(CreateView):
    model = Clientes
    form_class = ClienteForm
    template_name = "consultas.html"
    success_url = "/"

    def form_valid(self, form):
        return super().form_valid(form)


class MedicoCreateView(CreateView):
    model = Medicos
    form_class = MedicoForm
    template_name = "consultas.html"
    success_url = "/"

    def form_valid(self, form):
        return super().form_valid(form)


class ClienteMedicoCreateView(View):
    template_name = "consultas.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {"cliente_form": ClienteForm(), "medico_form": MedicoForm()},
        )

    def post(self, request, *args, **kwargs):
        cliente_form = ClienteForm(request.POST)
        medico_form = MedicoForm(request.POST)
        if cliente_form.is_valid() and medico_form.is_valid():
            with transaction.atomic():
                cliente = cliente_form.save()
                medico = medico_form.save()
            return redirect("consultas")
        else:
            return render(
                request,
                self.template_name,
                {"cliente_form": cliente_form, "medico_form": medico_form},
            )
