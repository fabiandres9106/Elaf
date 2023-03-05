from django import forms
from django.forms import ModelForm
from .models import Preinscripcion_legislacion

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class RegistroLegislacionForm(ModelForm):

    #FORMULARIO A PARTIR DEL MODELO
    class Meta:
        model = Preinscripcion_legislacion
        fields = ['nombres', 'apellidos', 'email', 'whatsapp', 'acepta_terminos_y_condiciones', 'suscripcion']

    #VALIDACIÓN EMAIL (Verifica si el email ya está registrado en la base de datos.)
    def clean_email(self):
        data = self.cleaned_data['email']
        emailbd = Preinscripcion_legislacion.objects.filter(email__iexact = data).exists()
        if emailbd:
            raise ValidationError(_('El email ya está registrado.'), code='Registrado')
        
        return data

