from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .forms import RegistroLegislacionForm
from .models import Preinscripcion_legislacion

from django.template.loader import get_template

from django.core.mail import EmailMultiAlternatives

# Create your views here.
def legislacion(request):

    args = {}

    if request.method == 'POST':
        form = RegistroLegislacionForm(request.POST)
        if form.is_valid():
            #Almacenamiento en BD
            nuevo_registro = form.save(commit=False)
            nuevo_registro.save()

            #Envío email confirmación
            mail = request.POST.get('email')
            nombres = request.POST.get('nombres')
            apellidos = request.POST.get('apellidos')
            mensaje = 'Registro'
            send_email(mail, nombres, apellidos, mensaje)

            #Retorna vista confirmación registro
            return render(request, 'confirmacion-registro.html')        
    else:
        form = RegistroLegislacionForm()

    args['form'] = form
    return render(request, 'registro-legislacion.html', args)


        
#Enviar email
def send_email(mail, nombres, apellidos, mensaje):
    context = {'mail': mail,
               'nombres': nombres,
               'apellidos': apellidos,
               'mensaje': mensaje}
    template = get_template('emails/email.html')
    content = template.render(context)
    
    asunto = descripcion = ''

    if mensaje == 'Registro':
        asunto = 'Registro Exitoso - Curso de Legislación Farmacéutica - Escuela Latinoamericana de Farmacia'
        descripcion = 'Tu registro en la Escuela Latinoamericana de Farmacia fue exitoso'

    email = EmailMultiAlternatives(
        asunto,
        descripcion,
        settings.EMAIL_HOST_USER,
        [mail]
    )

    email.attach_alternative(content, 'text/html')
    email.send()
        
        
        
        
        


        
        