from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from app.models import*

class Trainers_List(ListView):
    model=Trainer
    template_name='Trainers_List.html'

    context_object_name='TL'
    #queryset=Trainer.objects.filter(trainer_name='harshad')

    ordering=['trainer_name']