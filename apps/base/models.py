from django.db import models
from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField 

# Create your models here.

class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    logo = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Фотография",
        blank = True, null = True
    )

    logo_complex = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Фотография",
        blank = True, null = True
    )

    email = models.EmailField(
        max_length=255,
        verbose_name='Почта'
        )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    whatsapp = models.URLField(
        verbose_name='Whatspp URL',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram URL',
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name='Youtube URL',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook URL',
        blank=True, null=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Основная настройка"
            verbose_name_plural = "Основные настройки"

################################################################################################################################################################################

class SettingsPhone(models.Model):
    settings = models.ForeignKey(Settings, related_name='phone_title', on_delete=models.CASCADE)
    phone = models.CharField(
          max_length = 255,
          verbose_name = "Телефонный номер"
     )
    class Meta:
        unique_together = ('settings', 'phone')

################################################################################################################################################################################

class About(models.Model):
    image =  ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='about_image/',
        verbose_name="Фотография",
        blank = True, null = True
    )

    descriptions = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    def __str__(self):
        return self.descriptions
    
    class Meta:
            verbose_name = "О нас"
            verbose_name_plural = "О нас"

################################################################################################################################################################################

class Gallery(models.Model):
    title = models.CharField(
         max_length = 255,
         verbose_name = "Название"
    )
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "Галерея"
            verbose_name_plural = "Галерея"

class GalleryImage(models.Model):
    settings = models.ForeignKey(Gallery, related_name='gallery_image', on_delete=models.CASCADE)
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='gallery/',
        verbose_name="Фотография",
        blank = True, null = True
    )

    class Meta:
        unique_together = ('settings', 'image')

################################################################################################################################################################################
