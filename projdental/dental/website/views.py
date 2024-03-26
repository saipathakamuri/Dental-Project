#from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings as conf_settings

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
        
def service(request):
    return render(request, 'service.html')

def pricing(request):
    return render(request, 'price.html')

def team(request):
    return render(request, 'team.html')
def appointment(request):
    return render(request, 'appointment.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['message_name']
        email = request.POST['message_email']
        message = request.POST['message']
        
        #send email to default address
        send_mail(
            'Follow up required for - ' + name,
            message,
            email,
            [conf_settings.CONTACT_US_FORM_EMAIL_TO],
            fail_silently=False,
        )

        messages.success(request, f'Hi {name}, Thanks for contacting us. We will follow up with you within next few business days.')
        return redirect('contact')
    else:
        return render(request, 'contact.html')
    

#def home(request):
#	return render(request,'home.html',{})