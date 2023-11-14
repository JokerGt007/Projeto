from django.contrib import admin
from app.models import *
from .forms import *

# classe para exibir os livros inline: direto na interface que exibe o autor
class AnimaisInline(admin.TabularInline):  # ou admin.StackedInline que mostraria a exibição inline empilhada
    # model referente: Book
    model = Animais
    # form referente: BookForm
    form = AnimaisForm
    extra = 1  # numero de formularios vazios a serem exibidos

# classe para exibir os autores
class EcoAdmin(admin.ModelAdmin):
    # atributo inline para exibir os livros inline xD
    inlines = [AnimaisInline]

# classe para exibir os livros inline: direto na interface que exibe o autor
class EspecieInline(admin.TabularInline):  # ou admin.StackedInline que mostraria a exibição inline empilhada
    # model referente: Book
    model = Especie
    # form referente: BookForm
    form = EspecieForm
    extra = 1  # numero de formularios vazios a serem exibidos

# classe para exibir os autores
class RacaAdmin(admin.ModelAdmin):
    # atributo inline para exibir os livros inline xD
    inlines = [EspecieInline]



admin.site.register(Tipos_da_Hidrosfera)
admin.site.register(Raca,RacaAdmin)
admin.site.register(Especie)
admin.site.register(Animais)
admin.site.register(Ecossistemas,EcoAdmin)
admin.site.register(Quiz)
