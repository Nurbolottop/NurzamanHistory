from django.shortcuts import render,redirect
from django.core.mail import send_mail
from apps.contacts.models import Contact,ContactInfo
from apps.base.models import Settings
from apps.apartment import models


# Create your views here.
def catalog(request):
    #base
    settings = Settings.objects.latest("id")

    #apartment
    categories = models.Category.objects.all()
    category_id = request.GET.get('category')
    filtered_apartments = models.Apartment.objects.all()

    if category_id:
        filtered_apartments = filtered_apartments.filter(category__id=category_id)

    rooms = models.Rooms.objects.all()
    rooms_id = request.GET.get("room")
    filtered_rooms_apartments = filtered_apartments  # Создайте отдельную переменную для комнат

    if rooms_id:
        filtered_rooms_apartments = filtered_apartments.filter(room__id=rooms_id)


 
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

    return render(request,'catalog.html', locals())

def planing(request,id):
    #base
    settings = Settings.objects.latest("id")

    #apartment
    apartment = models.Apartment.objects.get(id=id)
    apartment_slide = models.Apartment.objects.all().order_by('?')[:5]


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
    return render(request, 'planing.html', locals())