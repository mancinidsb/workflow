from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    value = models.IntegerField(verbose_name="Valor")

    def __str__(self):
        return self.name
