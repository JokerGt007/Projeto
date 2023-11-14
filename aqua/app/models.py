from django.db import models

class Tipos_da_Hidrosfera(models.Model):
    id_tipo = models.IntegerField()
    nome = models.CharField(max_length=50)
    localizacao = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.localizacao}'

class Raca(models.Model):
    id_raca = models.IntegerField()
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}'
    
class Especie(models.Model):
    id_especie = models.IntegerField()
    nome = models.CharField(max_length=50)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}'
    

class Ecossistemas(models.Model):
    id_eco = models.IntegerField()
    nome = models.CharField(max_length=50)
    tamanho = models.FloatField()
    tipo = models.ForeignKey(Tipos_da_Hidrosfera, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome} {self.tamanho} {self.tipo}'


class Animais(models.Model):
    id_animal = models.IntegerField()
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    eco = models.ForeignKey(Ecossistemas, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.idade} {self.raca} {self.especie}'

class Quiz(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'self.nome'
