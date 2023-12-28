from django.shortcuts import render,redirect
from django.core.mail import send_mail
from apps.contacts.models import Contact
from apps.base.models import Settings,ContactInfo
from apps.apartment import models
from apps.telegram_bot.views import get_text
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def catalog(request):
    #base
    settings = Settings.objects.latest("id")

    # категории квартир
    categories = models.Category.objects.all()
    category_id = request.GET.get('category')
    apartments = models.Apartment.objects.all()

    # фильтрация квартир по категории
    if category_id:
        apartments = apartments.filter(category__id=category_id)

    # комнаты
    rooms = models.Rooms.objects.all()
    rooms_id = request.GET.get("room")

    # фильтрация отфильтрованных квартир по комнатам
    items_per_page = 4

    # Создание объекта Paginator
    paginator = Paginator(apartments, items_per_page)

    # Получение номера текущей страницы из GET-параметра
    page = request.GET.get('page')

    try:
        # Получение объекта Page для текущей страницы
        apartments = paginator.page(page)
    except PageNotAnInteger:
        # Если 'page' не является целым числом, отображаем первую страницу
        apartments = paginator.page(1)
    except EmptyPage:
        # Если 'page' больше максимального номера страницы, отображаем последнюю страницу
        apartments = paginator.page(paginator.num_pages)
        apartments = paginator.page(paginator.num_pages)

    # контактная информация
    contactinfo = ContactInfo.objects.latest('id')
    if request.method == "POST":
        if "call1" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            consent = request.POST.get('consent') == 'on'  # Проверка, что чекбокс был отмечен
            if consent:
                get_text(f"""
                Оставлена заявка на обратный звонок
                Имя пользователя: {name}
                emai: {email}
                Номер телефона: {number}""")
            if consent:
                contact = Contact.objects.create(name=name, email=email, number=number)
                send_mail(
                    f'{name}',
                    f'Здравствуйте {name}, Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}',
                    "noreply@somehost.local",
                    [email])
                return redirect('index')
        if "call2" in request.POST:
            name = request.POST.get('name2')
            email = request.POST.get('email2')
            number = request.POST.get('number2')
            consent = request.POST.get('consent2') == 'on'  # Проверка, что чекбокс был отмечен
            if consent:
                contact = Contact.objects.create(name=name, email=email, number=number)
                send_mail(
                    f'{name}',
                    f'Здравствуйте {name}, Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}',
                    "noreply@somehost.local",
                    [email])
                return redirect('index')

    return render(request, 'catalog.html', locals())

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