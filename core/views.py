from django.shortcuts import render
from django.views.generic import ListView, View
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import ProdutoModel
from .forms import ProdutoForm
# Create your views here.

class IndexView(ListView):
    model = ProdutoModel
    template_name = 'pages/index.html'
    context_object_name = 'products'
    
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        
        return queryset
    
    
class DeleteView(View):
    def get_produto(self, request, id):
        return get_object_or_404(ProdutoModel, id=id)

    def redirect_page(self):
        return redirect(reverse('index'))
    
    def post(self, request, id):
        produto = self.get_produto(request, id)
        produto.delete()
        
        return self.redirect_page()