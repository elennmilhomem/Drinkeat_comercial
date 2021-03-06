from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usuario(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    instagram = models.CharField(max_length=30, default=None)
    twitter = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    descricao_usuario = models.CharField(max_length=120)
    pontuacao = models.IntegerField(null=True)
    foto_perfil = models.ImageField(null=True)
    # usuario = models.ManyToManyField(Usuario)


class Estabelecimento(models.Model):
    nome_est = models.CharField(max_length=30)
    endereco_est = models.CharField(max_length=120)
    telefone_est = models.CharField(max_length=11)
    descricao_est = models.CharField(max_length=120)


class Avaliacao(models.Model):
    nota = models.IntegerField()
    data = models.DateField()
    comentario = models.CharField(max_length=240)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=30)
    nome_descricao = models.CharField(max_length=30)
    user = models.ManyToManyField(User)
    estabelecimento = models.ManyToManyField(Estabelecimento)


class Post(models.Model):
    data = models.DateField(null=True)
    imagem = models.ImageField(upload_to='images/', blank=True, null=True)
    comentario = models.CharField(max_length=240, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Desconto(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.FloatField()
    voucher = models.ImageField()
    estabelecimento = models.ForeignKey(
        Estabelecimento, on_delete=models.CASCADE)
    usuario = models.ManyToManyField(Usuario)
