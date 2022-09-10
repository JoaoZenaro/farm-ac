from django.db import models

# Create your models here.

class Tipo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

# class LancamentosRecorrentes(models.Model):
#     nome = models.CharField(max_length=255)
#     descricao = models.CharField(max_length=255)
#     valor = models.FloatField()
#     tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)
#     dataInicio = models.DateField(null=True, blank=True)
#     dataFim = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return self.nome

class Prestacao(models.Model):
    data = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.data)[0:len(str(self.data))-3]

class Lancamentos(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    valor = models.FloatField()
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    data = models.DateField(null=True, blank=True)

    prestacao = models.ForeignKey(Prestacao,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome