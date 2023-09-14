from bar import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import login, cadastro, contato
from carrinho.views import carrinho
from produtos.views.produto_view import home, produto
from produtos.views import produto_view
from produtos.api.produto import ProdutoViewSet
# from produtos.api import listarProdutoViewSet

routers = DefaultRouter()
routers.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('produto/', produto, name='produto'),
    path('usuarios/', include('usuarios.urls')),
    path('carrinho/', carrinho, name='carrinho'),
    path('api/', include(routers.urls)),
    ]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
