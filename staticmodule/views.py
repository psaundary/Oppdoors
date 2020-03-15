from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView ,FormView
from staticmodule.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
class MailSend(TemplateView):
    template_name='staticmodule/mailsend.html'
# Create your views here.
class MailNotSend(TemplateView):
    template_name='staticmodule/mailsend.html'

def contactus(request):
#     return render(request, 'staticmodule/contactus.html')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    from_email = request.POST.get('email')
    if subject and message and from_email:
        try:
            send_mail(from_email, subject+" \n"+message,settings.EMAIL_HOST_USER , ['welcomemailalankrati@gmail.com'])
        except BadHeaderError:
            return HttpResponseRedirect('mailnotsend/')
        return HttpResponseRedirect('mailsend/')
    else:
        print(subject,message,from_email)
        # In reality we'd use a form class
        # to get proper validation errors.
        return render(request, 'staticmodule/index.html')