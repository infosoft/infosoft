# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from forms import ContactForm
from django.core.mail import EmailMultiAlternatives # Enviamos HTML

def index(request):
    return render_to_response('home/index.html',context_instance=RequestContext(request))

def contacto(request):
    info_enviado = False # Definir si se envio la informacion o no se envio
    email = ""
    titulo = ""
    texto = ""
    if request.method == "POST":
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            info_enviado = True
            email = formulario.cleaned_data['Email']
            nombre =formulario.cleaned_data['Nombre']
            titulo = formulario.cleaned_data['Titulo']
            texto = formulario.cleaned_data['Texto']

            # Configuracion enviando mensaje via GMAIL
            to_admin = 'jimmyalcala@gmail.com'
            html_content = "Informacion recibida del Formulario de Contacto de Infosoft.net.ve por:[%s] [%s] <br><br><br>***Mensaje****<br><br>%s"%(nombre,email,texto)
            msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
            msg.attach_alternative(html_content,'text/html') # Definimos el contenido como HTML
            msg.send() # Enviamos  en correo
    else:
        formulario = ContactForm()
    ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
    return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))