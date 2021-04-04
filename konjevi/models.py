from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    nick_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    contraction_date = models.DateField(auto_now=True)
    address = models.CharField(max_length=100)
    function = models.CharField(max_length=20)
    contraction_time = models.IntegerField()
    identication_document = models.CharField(max_length=15)
    academic_level = models.CharField(max_length=20)


class Suplier(models.Model):
    first_name = models.CharField(max_length=30)
    nick_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    contraction_date = models.DateField(auto_now=True)
    address = models.CharField(max_length=100)
    function = models.CharField(max_length=20)


class Product(models.Model):
    name = models.CharField(max_length=100)
