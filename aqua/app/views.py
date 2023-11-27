from django.shortcuts import render
from .models import *

def consulta(request):
    ecossistemas = Ecossistemas.objects.prefetch_related('animais_set').all()

    consultas = {
        'ecossistemas': ecossistemas,
    }

    return render(request, 'consulta/consulta.html', consultas)

def quiz(request):
    quizs = {
        'quizs': Quiz.objects.all()
    }
    return render(request,'quiz/quiz.html', quizs)