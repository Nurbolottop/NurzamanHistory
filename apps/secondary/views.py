from django.shortcuts import render
from apps.contacts.models import Contact,ContactInfo
from apps.base.models import Settings
from django.shortcuts import render,redirect
from django.core.mail import send_mail

# Create your views here.
def genPlaning(request):
    #base
    settings = Settings.objects.latest("id")

    #contacts
    contactinfo = ContactInfo.objects.latest('id')
    if request.method == "POST":
        if "call1" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            consent = request.POST.get('consent') == 'on'  # Проверка, что чекбокс был отмечен
            if consent:
                contact = Contact.objects.create(name =name, email = email,number = number)
                send_mail(
                    f'{name}',
                    f'Здравствуйте {name},Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}',
                    "noreply@somehost.local",
                    [email])
                return redirect('index')
        if "call2" in request.POST:
            name = request.POST.get('name2')
            email = request.POST.get('email2')
            number = request.POST.get('number2')
            consent = request.POST.get('consent2') == 'on'  # Проверка, что чекбокс был отмечен
            if consent:
                contact = Contact.objects.create(name =name, email = email,number = number)
                send_mail(
                    f'{name}',
                    f'Здравствуйте {name},Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}',
                    "noreply@somehost.local",
                    [email])
            
                return redirect('index')

    return render(request,'genPlaning.html', locals())



