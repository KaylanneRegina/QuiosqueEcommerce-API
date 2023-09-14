from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from produtos.models.produto import Produto


def home(request):
    produtos = Produto.objects.all()
    context = {
        "produtos": produtos
    }
    return render(request, 'home.html', context)

def produto(request):
    return render(request, 'produto.html')

