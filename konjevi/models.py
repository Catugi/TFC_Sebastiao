from django.db import models


class User(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    apelidp = models.CharField(max_length=30, blank=True)
    ultimo_nome = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    data_contratacao = models.DateField(auto_now=True)
    endereco = models.CharField(max_length=100)
    funcao = models.CharField(max_length=20)
    tempo_contrato = models.IntegerField()
    documento_identificacao = models.CharField(max_length=15)
    nivel_academico = models.CharField(max_length=20)
    sexo = models.CharField(max_length=10)


class Client(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    apelidp = models.CharField(max_length=30, blank=True)
    ultimo_nome = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    proveniencia = models.CharField(max_length=30)
    sexo = models.CharField(max_length=10)


class Suplier(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    apelidp = models.CharField(max_length=30, blank=True)
    ultimo_nome = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    data_contratacao = models.DateField(auto_now=True)
    endereco = models.CharField(max_length=100)
    funcao = models.CharField(max_length=20)
    sexo = models.CharField(max_length=20)


class Product(models.Model):
    nome = models.CharField(max_length=100)


class Venda(models.Model):
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)


class Room(models.Model):
    tipo = models.CharField(max_length=20)


class Reserva(models.Model):
    quarto = models.ForeignKey(Room, on_delete=models.CASCADE)
    atendente = models.ForeignKey(User, on_delete=models.CASCADE)
