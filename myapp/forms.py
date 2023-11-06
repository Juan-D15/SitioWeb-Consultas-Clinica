from django import forms
from .models import Clientes, Medicos


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
            "nombre",
            "nacimiento",
            "dpi",
            "direccion",
            "telefono",
            "razon_visita",
            "receta_medica",
        ]


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = [
            "nombre_medico",
            "telefono_medico",
            "numero_colegiado",
            "especialidad",
            "diagnostico",
        ]
