from .models import Produto
from .serializers.produtos_serializers import ProdutoSerializer
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def listarProdutos(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    produtos = Produto.objects.all()
    produtos_serializers = ProdutoSerializer(produtos, many=True)
    return Response(produtos_serializers.data)

@api_view(['GET', 'PATCH'])
def detalharProduto(request, id):
    if request.method == 'GET':
        produto = Produto.objects.get(id=id)
        serializers = ProdutoSerializer(produto)
        return Response(serializers.data)
    elif request.method == 'PATCH':
        produto = Produto.objects.get(id=id)
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(produto, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
