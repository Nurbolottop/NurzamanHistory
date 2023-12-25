from django.db import models
from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField 

# Create your models here.
class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    number = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Запросы на связи"
        verbose_name_plural = "Запрос на связь"

################################################################################################################################################################################

class ContactInfo(models.Model):
    title = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='gallery/',
        verbose_name="Фотография",
        blank = True, null = True
    )

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Заказать обратный Звонок"
        verbose_name_plural = "Заказать обратный Звонок"