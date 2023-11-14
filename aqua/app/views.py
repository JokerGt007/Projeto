from django.shortcuts import render
from . models import *

def consulta(request):
    ecossistemas = Ecossistemas.objects.all()
    animais = Animais.objects.all()
    racas = Raca.objects.all()
    especies = Especie.objects.all()
    
    consultas = {
        'ecossistemas': ecossistemas,
        'animais': animais,
        'racas': racas,
        'especies': especies
    }
    
    return render(request, 'consulta/consulta.html', consultas)

def quiz(request):
    quizs = {
        'quizs': Quiz.objects.all()
    }
    return render(request,'quiz/quiz.html', quizs)