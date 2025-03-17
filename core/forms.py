from django import forms
from .models import ProdutoModel

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = ProdutoModel
        fields = '__all__'