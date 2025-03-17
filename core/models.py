from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class ProdutoModel(models.Model):
    name = models.CharField(("Nome"), max_length=50, unique=True)
    price = models.DecimalField(("Preço"), max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(("Imagem"), upload_to='image/product/%y/%m/%d', blank=True, null=True,)
    
    def __str__(self):
        return f'{self.name} - R$ {self.price:.2f}'