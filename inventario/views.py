from django.shortcuts import render
from .models import Produto

def valor_total_estoque(request):
    produtos = Produto.objects.all()
    total_estoque = sum(produto.valor_total() for produto in produtos)
    
    context = {
        'total_estoque': total_estoque,
        'produtos': produtos
    }
    
    return render(request, 'inventario/valor_total_estoque.html', context)
