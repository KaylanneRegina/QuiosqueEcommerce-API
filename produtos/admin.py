from django.contrib import admin


from produtos.models.produto import Produto
from produtos.models.categoria import Categoria

admin.site.register(Produto)
admin.site.register(Categoria)

