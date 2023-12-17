from django.shortcuts import render
from apps.base import models
from apps.secondary.models import Slide,Projects

# Create your views here.
def index(request):
    settings = models.Settings.objects.latest("id")
    slide = Slide.objects.latest('id')
    about = models.About.objects.latest('id')
    partners = Projects.objects.all()
    return render(request,'base/index.html', locals())
