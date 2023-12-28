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
    consent = models.BooleanField(
        default=False, 
        verbose_name="Согласие на обработку данных"
    )
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Запросы на связи"
        verbose_name_plural = "Запрос на связь"

################################################################################################################################################################################

