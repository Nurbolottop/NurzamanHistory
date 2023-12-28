from django.urls import path

from apps.secondary import views

urlpatterns = [
    path('genplaning/', views.genPlaning, name="genplaning"),
]
