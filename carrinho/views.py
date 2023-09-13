from django.shortcuts import render


def carrinho(request):
    if request.method == 'GET':
        return render(request, 'carrinho.html')
