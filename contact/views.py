from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.


def contact(request):
    # print("Petición: {}".format(request.method))
    contactForm = ContactForm()  # Instancia del formulario
    if request.method == "POST":
        contactForm = ContactForm(data=request.POST)
        # Capturar la información que se recibe desde la petición POST
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')
        # Redirecciona a la página que se indique
        # return redirect(reverse('contact)+"?ok")
        email = EmailMessage(
            "Abryl Ec: Nuevo mensaje de contacto",
            "De {} <{}>\n\nMensaje:\n\n{}".format(name, email, content),
            "no-contestar@inbox.mailtrap.io",
            ["abrylmusic@gmail.com"],
            reply_to=[email]
        )

        try:
            email.send()
            return redirect(reverse('contact')+"?ok")
        except:
            return redirect(reverse('contact')+"?fail")

    # Enviar mail

    return render(request, "contact/contact.html", {'contactForm': contactForm})
