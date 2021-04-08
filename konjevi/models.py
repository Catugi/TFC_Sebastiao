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


class TypeSuplier(models.Model):
    nome = models.CharField(max_length=30)


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
    fornedcedor = models.ForeignKey(Suplier, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=30)
    preco = models.FloatField()


class Venda(models.Model):
    nome_do_cliente = models.CharField(max_length=30)
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)


class Room(models.Model):
    categoria = models.CharField(max_length=20)
    preco = models.FloatField()


class Reserva(models.Model):
    quarto = models.ForeignKey(Room, on_delete=models.CASCADE)
    atendente = models.ForeignKey(User, on_delete=models.CASCADE)


class RentRoom(models.Model):
    estado = models.CharField(max_length=20)
    tempo_de_aluguel = models.IntegerField(blank=True)
    preco = models.FloatField()
    hora_de_entrada = models.DateTimeField(auto_now=True)