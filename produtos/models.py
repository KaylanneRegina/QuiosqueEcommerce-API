from django.db import models

# Create your models here.

class Produto(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    nome_produto = models.CharField(max_length=30)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    foto = models.ImageField(null=True, blank=True, upload_to='img_produtos', default='img_produtos/skol.png')

    def __str__(self):
        return self.nome_produto
        
