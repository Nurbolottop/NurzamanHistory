from django.shortcuts import render,redirect
from apps.base import models
from apps.secondary.models import Slide,Projects,Pride,Euro,Choise,Advantages,Environment,Street
from apps.contacts.models import Contact,ContactInfo
from django.core.mail import send_mail
# Create your views here.
def index(request):
    #BASE
    settings = models.Settings.objects.latest("id")
    about = models.About.objects.latest('id')
    gallery = models.Gallery.objects.latest('id')

    #SECONDARY
    slide = Slide.objects.latest('id')
    pride = Pride.objects.latest('id')
    projects = Projects.objects.all()
    euro = Euro.objects.latest("id")
    choise = Choise.objects.latest("id")
    advantages = Advantages.objects.latest("id")
    environment = Environment.objects.all()
    street = Street.objects.latest("id")
    

    #CONTACTS
    contactinfo = ContactInfo.objects.latest('id')
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        contact = Contact.objects.create(name =name, email = email,number = number)
        send_mail(
            f'{name}',

            f'Здравствуйте {name},Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}',
            "noreply@somehost.local",
            [email])
        
        return redirect('index')

    return render(request,'base/index.html', locals())

################################################################################################################################################################################
