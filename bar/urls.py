from django.contrib import admin
from django.urls import path, include
from produtos.views import home, produto
from usuarios.views import login, cadastro, contato
from carrinho.views import carrinho
from produtos.views import produto
from produtos.api import listarProdutos, detalharProduto

from django.conf.urls.static import static
from bar import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('produto/', include('produtos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('carrinho/', carrinho, name='carrinho'),
    path('api/produtos/', listarProdutos),
    path('api/produtos/<int:id>/', detalharProduto)
    ]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
