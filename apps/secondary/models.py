from django.db import models

# Create your models here.
class Slide(models.Model):
    image = models.ImageField(
        upload_to="slide_image",
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length =  255,
        verbose_name="Название"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Слайд"
        verbose_name_plural = "Слайды"

class Projects(models.Model):
    image = models.ImageField(
        upload_to="image_partners",
        verbose_name="Фотография"
    )

    class Meta:
        verbose_name="Партнер"
        verbose_name_plural = "Партнеры"