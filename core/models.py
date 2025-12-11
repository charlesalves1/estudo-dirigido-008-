from django.db import models

class Unidade(models.Model):
    nome = models.CharField(max_length=120)
    endereco = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome


class Sala(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="salas")
    nome = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.unidade.nome} - {self.nome}"


class Status(models.Model):
    nome = models.CharField(max_length=100)   
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategorias')

    def __str__(self):
        return self.nome


class Bem(models.Model):
    nome = models.CharField(max_length=200)
    tombo = models.CharField(max_length=50, unique=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name="bens")
    sala = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.tombo})"