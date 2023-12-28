from django.db import models
from django_resized.forms import ResizedImageField 

# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название категории",
        blank= True, null = True

    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория квартир"
        verbose_name_plural = "Категория квартир"



################################################################################################################################################################################

class Rooms(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Сколько Комнат"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Добавить Комнаты"
        verbose_name_plural = "Добавить Комнаты"

################################################################################################################################################################################

class Floor(models.Model):
    title = models.CharField(
        max_length = 2,
        verbose_name = "Номер этажа"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Добавить Этажи"
        verbose_name_plural = "Добавить Этажи"

################################################################################################################################################################################

class Status(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Статус квартиры"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Добавить Статус"
        verbose_name_plural = "Добавить Статус"
        
################################################################################################################################################################################

class Apartment(models.Model):
    category = models.ForeignKey(
        Category,
        related_name = "category_room",
        on_delete = models.CASCADE,
        blank= True, null = True
    )
    room = models.ForeignKey(
        Rooms,
        on_delete = models.CASCADE
    )
    razmer = models.CharField(
        max_length = 255,
        verbose_name = "Размер"
    )
    info = models.CharField(
        max_length = 255,
        verbose_name ="Дополнительная информация",
        blank = True,null=True

    )
    layote = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='layote/',
        verbose_name="Фотография планировки",
        blank = True, null = True
    )
    plan = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='plan/',
        verbose_name="Фотография на плане этажа",
        blank = True, null = True
    )
    object = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='object/',
        verbose_name="Фотография на объекте",
        blank = True, null = True
    )
    price = models.CharField(
        max_length = 255,
        verbose_name = "Цена"
    )
    floor = models.ForeignKey(
        Floor,
        related_name = "floor_form",
        on_delete = models.CASCADE,
        verbose_name = "Сколько этаж",
        blank=True,null = True
    )
    exploitation = models.CharField(
        max_length = 255,
        verbose_name = "Ввод в эксплуатацию"
    )
    layout_text = models.CharField(
        max_length = 255,
        verbose_name = "Тип планировок "
    )
    status = models.ForeignKey(
        Status,
        related_name = "choise_room",
        on_delete = models.CASCADE,
        blank = True, null = True
    )
    def __str__(self):
        return self.info

    class Meta:
        verbose_name = "Добавить Квартиру"
        verbose_name_plural = "Добавить Квартиру"

class ApartmentOsob(models.Model):
    settings = models.ForeignKey(Apartment, related_name='choise_image', on_delete=models.CASCADE)
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        unique_together = ('settings', 'title')
        verbose_name = "Добавить Особенности"
        verbose_name_plural = "Добавить Особенности"
################################################################################################################################################################################
