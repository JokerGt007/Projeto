from django import forms
from .models import *

# inicializando um formulario para os livros
class EspecieForm(forms.ModelForm):
    class Meta:
        # modelo referente: Book
        model = Especie
        # atribuindo todos os campos do modelo Book ao Form
        fields = '__all__'

class AnimaisForm(forms.ModelForm):
    class Meta:
        # modelo referente: Book
        model = Animais
        # atribuindo todos os campos do modelo Book ao Form
        fields = '__all__'