from django.db import models
from django.contrib.auth.models import User

class Tipo(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    foto = models.ImageField(upload_to='foto_evento', null=True, blank=True)
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    data_inicial = models.DateTimeField(auto_now_add=False)
    data_final = models.DateTimeField(auto_now_add=False)
    local = models.CharField(max_length=100)

    def __str__(self):
         return f' {self.foto} {self.nome} - {self.tipo} - {self.data_inicial} - {self.data_final} -{self.local} '

class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.nome} - {self.sobrenome} - {self.cpf} - {self.email} -{self.evento} '

# class Submissao(models.Model):
#     nome = models.ForeignKey(Inscricao)


