from django.contrib import admin

# Register your models here.
from produtos.models import Produto

admin.site.register(Produto)
