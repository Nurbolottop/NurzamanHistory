from django.shortcuts import render,redirect
from django.core.mail import send_mail
from apps.contacts.models import Contact,Messages,View
from apps.base.models import Settings,ContactInfo
from apps.apartment import models
from apps.telegram_bot.views import get_text
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from apps.apartment.forms import ApartmentSearchForm

# Create your views here.
def catalog(request):
    #base
    settings = Settings.objects.latest("id")
    apartments = models.Apartment.objects.all()

    # категории квартир
    categories = models.Category.objects.all()
    category_id = request.GET.get('category')

    # фильтрация квартир по категории
    if category_id:
        apartments = apartments.filter(category__id=category_id)

# Инициализация формы поиска
    search_form = ApartmentSearchForm(request.GET or None)

    # Обработка AJAX-запроса
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if search_form.is_valid():
            apartments = apartments.filter(
                price__gte=search_form.cleaned_data.get('min_price', 0),
                price__lte=search_form.cleaned_data.get('max_price', 1000000000),
                razmer__gte=search_form.cleaned_data.get('min_size', 0),
                razmer__lte=search_form.cleaned_data.get('max_size', 1000),
                floor__title__gte=search_form.cleaned_data.get('min_floor', 0),
                floor__title__lte=search_form.cleaned_data.get('max_floor', 11),
           
            )
            apartments_data = list(apartments.values(
            'id', 
            'category__title', 
            'info',
            'room__title', 
            'status__title', 
            'razmer', 
            'price',
            'layote',  # убедитесь, что это поле существует в модели
            'floor__title',  # убедитесь, что это поле существует в модели
            # Добавьте другие поля, которые вы хотите отправить
            ))
            for apt in apartments_data:
                apt['layote_url'] = apt['layote'] and getattr(models.Apartment.objects.get(pk=apt['id']).layote, 'url', '')
            return JsonResponse({'results': apartments_data}, safe=False)
        else:
            return JsonResponse({'error': search_form.errors}, status=400)
    # комнаты
    rooms = models.Rooms.objects.all()
    rooms_id = request.GET.get("room")

    if rooms_id:
        apartments = apartments.filter(room_id=rooms_id)

    # контактная информация
    contactinfo = ContactInfo.objects.latest('id')
    if request.method == "POST":
        if "call1" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            consent = request.POST.get('consent') == 'on'  # Проверка, что чекбокс был отмечен
            if consent:
                contact = Contact.objects.create(name=name, email=email, number=number)
                send_mail(
                    f'{name}',
                    f'Здравствуйте {name}, Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}',
                    "noreply@somehost.local",
                    [email])
            if consent:
                get_text(f"""
                ✅Оставлена заявка на обратный звонок
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {number}""")
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
            if consent:
                get_text(f"""
                ✅Оставлена заявка на обратный звонок🤗
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {number}""")
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
                contact = Contact.objects.create(name=name, email=email, number=number)
                send_mail(
                    f'{name}',
                    f'Здравствуйте {name}, Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}',
                    "noreply@somehost.local",
                    [email])
            if consent:
                get_text(f"""
                ✅Пользователь оставил заявку на  обратный звонок
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {number}""")
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
            if consent:
                get_text(f"""
                ✅Пользователь оставил заявку на  обратный звонок
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {number}""")
                return redirect('index')
            
        if "quations" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            consent = request.POST.get('consent') == 'on'  # Проверка, что чекбокс был отмечен
            if consent:
                contact = Messages.objects.create(name=name, email=email, phone=phone,message=message)
                send_mail(
                    f'{name}',
                    f'Здравствуйте {name}, Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}. Ваш вопрос: {message}' ,
                    "noreply@somehost.local",
                    [email])
            if consent:
                get_text(f"""
                ✅Пользователь задал вопрос
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {phone}

Вопрос: <b>{message}</b>""")
                return redirect('index')
            
        if "views" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            consent = request.POST.get('consent') == 'on'  # Проверка, что чекбокс был отмечен
            if consent:
                contact = Messages.objects.create(name=name, email=email, phone=phone,message=message)
                send_mail(
                    f'{name}',
                    f'Здравствуйте {name}, Спасибо за обратную связь, Мы скоро свами свяжемся. Ваша почта: {email}. Ваш вопрос: {message}' ,
                    "noreply@somehost.local",
                    [email])
            if consent:
                get_text(f"""
                ✅Пользователь оставил заявку на просмотр
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {name}
emai: {email}
Номер телефона: {phone}

Коментарий: <b>{message}</b>""")
                return redirect('index')
    return render(request, 'planing.html', locals())