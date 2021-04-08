from django.db import models


class User(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    apelido = models.CharField(max_length=30, blank=True)
    ultimo_nome = models.CharField(max_length=30)
    nacionalidade = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    data_contratacao = models.DateField(auto_now=True)
    endereco = models.CharField(max_length=100)
    funcao = models.CharField(max_length=20)
    tempo_contrato = models.CharField(max_length=30)
    documento_identificacao = models.CharField(max_length=15)
    nivel_academico = models.CharField(max_length=20)
    sexo = models.CharField(max_length=10)
    fotografia = models.ImageField(upload_to="images")


class Client(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    apelido = models.CharField(max_length=30, blank=True)
    ultimo_nome = models.CharField(max_length=30)
    nacionalidade = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    documento_identificacao = models.CharField(max_length=10)
    num_documento_identificacao = models.CharField(max_length=15)
    proveniencia = models.CharField(max_length=30)
    sexo = models.CharField(max_length=10)


class Suplier(models.Model):
    tipo = models.CharField(max_length=30)
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)


class Product(models.Model):
    fornecedor = models.ForeignKey(Suplier, on_delete=models.CASCADE)
    origem = models.CharField(max_length=30)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=30)
    preco = models.FloatField()


class Venda(models.Model):
    nome_do_cliente = models.CharField(max_length=30)
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)
    imprimir_factura = models.BooleanField(default=True)


class Room(models.Model):
    categoria = models.CharField(max_length=20)
    preco = models.FloatField()


class Reserva(models.Model):
    atendente = models.ForeignKey(User, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Room, on_delete=models.CASCADE)
    atendente = models.ForeignKey(User, on_delete=models.CASCADE)
    imprimir_factura = models.BooleanField(default=True)


class RentRoom(models.Model):
    atendente = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)
    tempo_de_aluguel = models.IntegerField(blank=True)
    preco = models.FloatField()
    hora_de_entrada = models.DateTimeField(auto_now=True)
    imprimir_factura = models.BooleanField(default=True)


class ServicosAuxiliares(models.Model):
    tipo = models.CharField(max_length=30)
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.DateTimeField()
    hora_termino = models.DateTimeField()
    descricao = models.TextField()